from portfolio_admin.models import Skill
from rest_framework import serializers


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        exclude = ['id', 'created_at', 'updated_at', 'portfolio']
