from django.contrib import admin
from .models import Cart, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem
    fields = ["variant", "quantity"]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["user", "total_items", "created_at"]
    inlines = [CartItemInline]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ["cart", "variant", "quantity", "subtotal"]
    list_editable = ["quantity"]
