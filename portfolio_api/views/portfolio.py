from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..serializers import PortfolioSerializer, Portfolio


class PortfolioViewSet(APIView):
    def get(self, request, name, format=None):
        portfolio = get_object_or_404(Portfolio, name=name, private=False)
        serializer = PortfolioSerializer(
            portfolio, context={'request': request}
        )
        return Response(serializer.data)
