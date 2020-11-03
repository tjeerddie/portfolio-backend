from rest_framework import viewsets
# from rest_framework.response import Response
from ..serializers import ProjectSerializer, Project


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        name = self.kwargs["portfolio_pk"].replace("_", " ")
        return Project.objects.filter(
            portfolio__name=name,
            private=False
        )
