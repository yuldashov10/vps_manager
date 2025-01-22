from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from users.constants import NULL_BLANK_TRUE, USER_FIRST_NAME_MAX_LENGTH
from users.managers import UserManager


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(
        "Email",
        unique=True,
    )
    first_name = models.CharField(
        "Имя",
        max_length=USER_FIRST_NAME_MAX_LENGTH,
    )
    avatar = models.ImageField(
        "Фото профиля",
        upload_to="avatars/",
        **NULL_BLANK_TRUE,
    )
    is_staff = models.BooleanField(
        "Является администратором",
        default=False,
    )
    is_active = models.BooleanField(
        "Активированный профиль",
        default=False,
    )

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("email",)

    def __str__(self) -> str:
        return f"{self.first_name} | {self.email}"
