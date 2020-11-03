from rest_framework import viewsets
from ..serializers import SkillSerializer, Skill


class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SkillSerializer

    def get_queryset(self):
        name = self.kwargs["portfolio_pk"].replace("_", " ")
        return Skill.objects.filter(
            portfolio__name=name,
        )
