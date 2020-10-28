from django.urls import path
from .views import ApiRootView, PortfolioViewSet


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', ApiRootView.as_view()),
    path('portfolio/<name>/', PortfolioViewSet.as_view()),
]
