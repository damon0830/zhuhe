from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"
        read_only_fields = ["id", "order", "subtotal"]


class OrderListSerializer(serializers.ModelSerializer):
    """列表用 — 精简"""
    items_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Order
        fields = [
            "id", "order_number", "status", "total", "currency",
            "items_count", "created_at", "paid_at",
        ]


class OrderDetailSerializer(serializers.ModelSerializer):
    """详情用 — 完整"""
    items = OrderItemSerializer(many=True, read_only=True)
    items_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Order
        fields = [
            "id", "order_number", "user", "email", "status",
            "shipping_address", "billing_address",
            "subtotal", "shipping_cost", "tax", "total", "currency",
            "items", "items_count", "notes",
            "created_at", "updated_at", "paid_at",
        ]


class CreateOrderSerializer(serializers.Serializer):
    """创建订单 — 从购物车转换"""
    shipping_address_id = serializers.IntegerField(required=False)
    shipping_address = serializers.JSONField(required=False)
    notes = serializers.CharField(required=False, allow_blank=True)

    def validate(self, attrs):
        if not attrs.get("shipping_address_id") and not attrs.get("shipping_address"):
            raise serializers.ValidationError("请提供收货地址")
        return attrs
