from portfolio_admin.models import Portfolio
from rest_framework import serializers


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        exclude = ['user']
