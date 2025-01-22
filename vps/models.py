import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from vps.constants import (
    MAX_CPU_COUNT,
    MAX_HDD_SIZE_GB,
    MAX_RAM_SIZE_MB,
    MIN_CPU_COUNT,
    MIN_HDD_SIZE_GB,
    MIN_RAM_SIZE_MB,
    VPS_STATUS_MAX_LENGTH,
)


class StatusVPS(models.TextChoices):
    STARTED = ("started", "Started")
    BLOCKED = ("blocked", "Blocked")
    STOPPED = ("stopped", "Stopped")


class VPS(models.Model):
    uid = models.UUIDField(
        "ID сервера",
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    cpu = models.PositiveSmallIntegerField(
        "Количество процессоров",
        default=MIN_CPU_COUNT,
        validators=[
            MinValueValidator(MIN_CPU_COUNT),
            MaxValueValidator(MAX_CPU_COUNT),
        ],
    )
    ram = models.PositiveSmallIntegerField(
        "Объем оперативной памяти (Мб)",
        default=MIN_RAM_SIZE_MB,
        validators=[
            MinValueValidator(MIN_RAM_SIZE_MB),
            MaxValueValidator(MAX_RAM_SIZE_MB),
        ],
    )
    hdd = models.PositiveSmallIntegerField(
        "Объем жесткого диска (Гб)",
        default=MIN_HDD_SIZE_GB,
        validators=[
            MinValueValidator(MIN_HDD_SIZE_GB),
            MaxValueValidator(MAX_HDD_SIZE_GB),
        ],
    )
    status = models.CharField(
        "Статус",
        max_length=VPS_STATUS_MAX_LENGTH,
        choices=StatusVPS.choices,
        default=StatusVPS.STARTED,
    )

    class Meta:
        verbose_name = "VPS сервер"
        verbose_name_plural = "VPS серверы"
        ordering = ("status",)

    def __str__(self) -> str:
        return f"{self.uid} - {self.status}"
