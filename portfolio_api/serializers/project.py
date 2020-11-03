from portfolio_admin.models import Project
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = ['id', 'created_at', 'updated_at', 'portfolio']
