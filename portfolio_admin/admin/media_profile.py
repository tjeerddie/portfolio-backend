from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from ..models import MediaProfile


@admin.register(MediaProfile)
class MediaProfileAdmin(admin.ModelAdmin):
    list_display = ("network", "username", "url", "private")
