from django.db import models
from django.conf import settings


class Cart(models.Model):
    """购物车 — 每个用户一个购物车"""
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="cart", verbose_name="用户"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = "购物车"

    def __str__(self):
        return f"Cart({self.user.email})"

    @property
    def total_items(self):
        return sum(item.quantity for item in self.items.all())

    @property
    def total_price(self):
        return sum(item.subtotal for item in self.items.all())


class CartItem(models.Model):
    """购物车条目"""
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="items",
        verbose_name="购物车"
    )
    variant = models.ForeignKey(
        "products.ProductVariant", on_delete=models.CASCADE,
        verbose_name="SKU", related_name="cart_items"
    )
    quantity = models.PositiveIntegerField("数量", default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "购物车项"
        verbose_name_plural = "购物车项"
        unique_together = ["cart", "variant"]

    def __str__(self):
        return f"{self.variant.sku} x{self.quantity}"

    @property
    def subtotal(self):
        return self.variant.price * self.quantity
