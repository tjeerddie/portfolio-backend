from rest_framework.views import APIView
from rest_framework.response import Response


class UrlView(APIView):
    def get(self, request, format=None):
        url = request.build_absolute_uri('/')
        return Response([
            f"{url}users"
        ])
