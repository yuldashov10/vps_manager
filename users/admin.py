from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ("email", "first_name", "is_active")
    list_filter = ("is_active", "is_staff")
    search_fields = ("email",)
    ordering = ("email",)
    fieldsets = (
        (
            None,
            {"fields": ("email", "password")},
        ),
        (
            "Личные данные",
            {
                "fields": (
                    "first_name",
                    "avatar",
                )
            },
        ),
        (
            "Разрешения",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            "Дата и время",
            {"fields": ("last_login", "date_joined")},
        ),
    )
