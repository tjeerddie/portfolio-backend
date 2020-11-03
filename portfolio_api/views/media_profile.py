from rest_framework import viewsets
from ..serializers import MediaProfileSerializer, MediaProfile


class MediaProfileViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MediaProfileSerializer

    def get_queryset(self):
        name = self.kwargs["portfolio_pk"].replace("_", " ")
        return MediaProfile.objects.filter(
            portfolio__name=name,
            private=False
        )
