from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ["sku", "product_name", "price", "quantity", "subtotal"]
    readonly_fields = ["subtotal"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["order_number", "user", "status", "total", "currency", "items_count", "created_at"]
    list_editable = ["status"]
    list_filter = ["status", "currency", "created_at"]
    search_fields = ["order_number", "user__email", "email"]
    inlines = [OrderItemInline]
    readonly_fields = ["order_number", "subtotal", "total", "paid_at"]
    fieldsets = [
        ("基本信息", {"fields": ["order_number", "user", "email", "status", "currency"]}),
        ("金额", {"fields": ["subtotal", "shipping_cost", "tax", "total"]}),
        ("地址", {"fields": ["shipping_address", "billing_address"]}),
        ("时间", {"fields": ["created_at", "updated_at", "paid_at"]}),
    ]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "sku", "product_name", "price", "quantity", "subtotal"]
    search_fields = ["sku", "product_name"]
