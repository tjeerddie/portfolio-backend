from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from ..models import Skill


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "summary", "view_projects_link")

    def view_projects_link(self, obj):
        print(obj.projects)
        count = obj.projects.count()
        url = (
            reverse("admin:portfolio_admin_project_changelist")
            + "?"
            + urlencode({"skills__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Projects</a>', url, count)

    view_projects_link.short_description = "Projects"
