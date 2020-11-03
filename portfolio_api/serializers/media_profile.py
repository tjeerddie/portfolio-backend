from portfolio_admin.models import MediaProfile
from rest_framework import serializers


class MediaProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaProfile
        exclude = ['id', 'created_at', 'updated_at', 'portfolio', 'private']
