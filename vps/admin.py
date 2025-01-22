from django.contrib import admin

from vps.constants import MAX_VALUES_PER_PAGE
from vps.models import VPS


@admin.register(VPS)
class VPSAdmin(admin.ModelAdmin):
    list_display = ("uid", "status", "ram", "hdd")
    list_filter = ("status",)
    list_editable = ("status", "ram", "hdd")
    search_fields = ("uid",)
    list_per_page = MAX_VALUES_PER_PAGE
