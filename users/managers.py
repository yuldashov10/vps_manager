from typing import Optional

from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(
        self,
        email: str,
        password: Optional[str] = None,
        **extra_fields,
    ):
        if not email:
            raise ValueError("Поле email обязательное")

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(
        self,
        email: str,
        password: Optional[str] = None,
        **extra_fields,
    ):
        superuser_required_fields: tuple[str, ...] = (
            "is_active",
            "is_staff",
            "is_superuser",
        )
        for field in superuser_required_fields:
            extra_fields.setdefault(field, True)
