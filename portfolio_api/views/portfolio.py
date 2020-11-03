from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from ..serializers import PortfolioSerializer, Portfolio


class PortfolioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

    def retrieve(self, request, pk):
        name = pk.replace("_", " ")
        portfolio = get_object_or_404(
            Portfolio, name__iexact=name, private=False)
        serializer = self.serializer_class(
            portfolio, context={'request': request},
        )
        return Response(serializer.data)
