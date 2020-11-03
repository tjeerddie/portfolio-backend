from portfolio_admin.models import Portfolio
from rest_framework import serializers
from rest_framework.reverse import reverse

view_name = "portfolio-projects-list"


class PortfolioSerializer(serializers.ModelSerializer):
    projects_url = serializers.SerializerMethodField()

    def get_projects_url(self, instance):
        url_kwargs = {'portfolio_pk': instance.name.replace(" ", "_")}
        return reverse(
            view_name, kwargs=url_kwargs, request=self.context["request"]
        )

    class Meta:
        model = Portfolio
        exclude = ['user', 'created_at', 'updated_at']
