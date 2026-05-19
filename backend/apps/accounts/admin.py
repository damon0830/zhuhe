from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Address


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ["email", "username", "preferred_language", "is_active", "date_joined"]
    list_filter = ["preferred_language", "is_active", "is_staff"]
    fieldsets = BaseUserAdmin.fieldsets + (
        ("额外信息", {"fields": ("phone", "avatar", "preferred_language")}),
    )


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ["recipient_name", "user", "country", "city", "is_default"]
    list_filter = ["country", "is_default"]
    search_fields = ["recipient_name", "user__email"]
