from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from ..models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "position", "view_skills_link",
                    "private", "start_date", "end_date")

    def view_skills_link(self, obj):
        count = obj.skills.count()
        url = (
            reverse("admin:portfolio_admin_skill_changelist")
            + "?"
            + urlencode({"projects__id": f"{obj.id}"})
        )
        return format_html(f'<a href="{url}">{count} Skills</a>')

    view_skills_link.short_description = "Skills"
