# Generated by Django 4.2 on 2025-01-22 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vps", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vps",
            name="status",
            field=models.CharField(
                choices=[
                    ("started", "Started"),
                    ("blocked", "Blocked"),
                    ("stopped", "Stopped"),
                ],
                default="started",
                max_length=7,
                verbose_name="Статус",
            ),
        ),
    ]
