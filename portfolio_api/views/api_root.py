from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import Portfolio


class ApiRootView(APIView):
    def get(self, request, format=None):
        url = request.build_absolute_uri('/')
        portfolio_urls = [
            f"{url}portfolio/{portfolio.name.replace(' ', '_')}/"
            for portfolio in Portfolio.objects.filter(private=False)
        ]
        return Response([*portfolio_urls])
