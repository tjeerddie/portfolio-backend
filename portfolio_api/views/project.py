from rest_framework import viewsets
# from rest_framework.response import Response
from ..serializers import ProjectSerializer, Project


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(
            portfolio__name=self.kwargs["portfolio_pk"]
        )
