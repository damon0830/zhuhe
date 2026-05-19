from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """自定义用户模型"""
    email = models.EmailField("邮箱", unique=True)
    phone = models.CharField("手机号", max_length=20, blank=True)
    avatar = models.ImageField("头像", upload_to="avatars/", blank=True)

    # 收货地址
    default_address = models.OneToOneField(
        "Address", on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name="默认地址", related_name="+"
    )

    # 偏好
    preferred_language = models.CharField("偏好语言", max_length=10, default="zh",
                                          choices=[("zh", "中文"), ("en", "English"), ("fr", "Français"), ("de", "Deutsch")])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"
        ordering = ["-date_joined"]

    def __str__(self):
        return self.email or self.username


class Address(models.Model):
    """收货地址"""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="addresses",
        verbose_name="用户"
    )
    recipient_name = models.CharField("收件人", max_length=100)
    phone = models.CharField("电话", max_length=20)

    # 国际地址
    country = models.CharField("国家", max_length=100, default="France")
    province = models.CharField("省/州", max_length=100, blank=True)
    city = models.CharField("城市", max_length=100)
    district = models.CharField("区", max_length=100, blank=True)
    address_line1 = models.CharField("地址1", max_length=255)
    address_line2 = models.CharField("地址2", max_length=255, blank=True)
    postal_code = models.CharField("邮编", max_length=20)

    is_default = models.BooleanField("默认地址", default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "收货地址"
        verbose_name_plural = "收货地址"
        ordering = ["-is_default", "-created_at"]

    def __str__(self):
        return f"{self.recipient_name} - {self.address_line1[:30]}"
