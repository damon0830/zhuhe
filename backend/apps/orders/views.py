from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.cart.models import Cart
from apps.accounts.models import Address
from apps.products.models import ProductVariant
from .models import Order, OrderItem
from .serializers import (
    OrderListSerializer, OrderDetailSerializer, CreateOrderSerializer
)


class OrderListView(generics.ListAPIView):
    """订单列表"""
    serializer_class = OrderListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderDetailView(generics.RetrieveAPIView):
    """订单详情"""
    serializer_class = OrderDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class CreateOrderView(APIView):
    """创建订单（从购物车结账）"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = CreateOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        cart = Cart.objects.filter(user=user).first()
        if not cart or not cart.items.exists():
            return Response({"detail": "购物车为空"}, status=status.HTTP_400_BAD_REQUEST)

        # 地址
        addr_id = serializer.validated_data.get("shipping_address_id")
        if addr_id:
            try:
                addr = Address.objects.get(id=addr_id, user=user)
                shipping_addr = {
                    "recipient_name": addr.recipient_name,
                    "phone": addr.phone,
                    "country": addr.country,
                    "province": addr.province,
                    "city": addr.city,
                    "address_line1": addr.address_line1,
                    "address_line2": addr.address_line2,
                    "postal_code": addr.postal_code,
                }
            except Address.DoesNotExist:
                return Response({"detail": "地址不存在"}, status=status.HTTP_404_NOT_FOUND)
        else:
            shipping_addr = serializer.validated_data["shipping_address"]

        # 计算金额
        subtotal = sum(item.subtotal for item in cart.items.all())
        shipping_cost = 0 if subtotal >= 200 else 15  # 满200包邮
        tax = round(subtotal * 0.20, 2)  # EU VAT 20%
        total = subtotal + shipping_cost + tax

        # 创建订单
        order = Order.objects.create(
            user=user,
            email=user.email,
            shipping_address=shipping_addr,
            billing_address=shipping_addr,
            subtotal=subtotal,
            shipping_cost=shipping_cost,
            tax=tax,
            total=total,
            notes=serializer.validated_data.get("notes", ""),
        )

        # 创建订单商品 (快照)
        for cart_item in cart.items.all():
            variant = cart_item.variant
            OrderItem.objects.create(
                order=order,
                variant=variant,
                product_name=variant.product.name,
                variant_name=variant.name,
                sku=variant.sku,
                price=variant.price,
                quantity=cart_item.quantity,
            )

        # 扣减库存
        for cart_item in cart.items.all():
            variant = cart_item.variant
            if variant.stock >= cart_item.quantity:
                variant.stock -= cart_item.quantity
                variant.save()
            else:
                # 库存不足 — 取消订单
                order.status = Order.Status.CANCELLED
                order.save()
                return Response({
                    "detail": f"{variant.sku} 库存不足",
                    "order": OrderDetailSerializer(order).data,
                }, status=status.HTTP_400_BAD_REQUEST)

        # 清空购物车
        cart.items.all().delete()

        return Response(OrderDetailSerializer(order).data, status=status.HTTP_201_CREATED)


class CancelOrderView(APIView):
    """取消订单"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            order = Order.objects.get(id=pk, user=request.user)
        except Order.DoesNotExist:
            return Response({"detail": "订单不存在"}, status=status.HTTP_404_NOT_FOUND)

        if order.status not in (Order.Status.PENDING, Order.Status.CONFIRMED):
            return Response({"detail": "当前状态不可取消"}, status=status.HTTP_400_BAD_REQUEST)

        # 恢复库存
        for item in order.items.all():
            if item.variant:
                item.variant.stock += item.quantity
                item.variant.save()

        order.status = Order.Status.CANCELLED
        order.save()

        return Response(OrderDetailSerializer(order).data)
