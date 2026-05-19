from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.products.models import ProductVariant
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer, AddToCartSerializer


def get_or_create_cart(user):
    cart, _ = Cart.objects.get_or_create(user=user)
    return cart


class CartDetailView(generics.RetrieveAPIView):
    """获取购物车详情"""
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return get_or_create_cart(self.request.user)


class AddToCartView(APIView):
    """添加商品到购物车"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = AddToCartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cart = get_or_create_cart(request.user)
        variant = ProductVariant.objects.get(
            id=serializer.validated_data["variant_id"],
            is_active=True
        )
        item, created = CartItem.objects.get_or_create(
            cart=cart,
            variant=variant,
            defaults={"quantity": serializer.validated_data["quantity"]}
        )
        if not created:
            item.quantity += serializer.validated_data["quantity"]
            item.save()
        return Response(CartItemSerializer(item).data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)


class UpdateCartItemView(APIView):
    """更新购物车项数量"""
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, item_id):
        cart = get_or_create_cart(request.user)
        try:
            item = CartItem.objects.get(id=item_id, cart=cart)
        except CartItem.DoesNotExist:
            return Response({"detail": "购物车项不存在"}, status=status.HTTP_404_NOT_FOUND)
        quantity = request.data.get("quantity")
        if quantity is not None:
            if quantity <= 0:
                item.delete()
                return Response({"detail": "已移除"}, status=status.HTTP_200_OK)
            item.quantity = quantity
            item.save()
        return Response(CartItemSerializer(item).data)


class RemoveFromCartView(APIView):
    """从购物车移除"""
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, item_id):
        cart = get_or_create_cart(request.user)
        CartItem.objects.filter(id=item_id, cart=cart).delete()
        return Response({"detail": "已移除"}, status=status.HTTP_200_OK)


class ClearCartView(APIView):
    """清空购物车"""
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        cart = get_or_create_cart(request.user)
        cart.items.all().delete()
        return Response({"detail": "购物车已清空"}, status=status.HTTP_200_OK)
