from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from ..models import Skill


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "summary", "view_projects_link")

    def view_projects_link(self, obj):
        count = obj.projects.count()
        url = (
            reverse("admin:portfolio_admin_project_changelist")
            + "?"
            + urlencode({"skills__id": f"{obj.id}"})
        )
        return format_html(f'<a href="{url}">{count} Projects</a>')

    view_projects_link.short_description = "Projects"
