from django.urls import path, include
from rest_framework_nested import routers
from .views import ApiRootView, PortfolioViewSet, ProjectViewSet, SkillViewSet

router = routers.SimpleRouter()
router.register(r'portfolio', PortfolioViewSet)
portfolio_router = routers.NestedSimpleRouter(
    router, r'portfolio', lookup='portfolio'
)
portfolio_router.register(
    r"projects",
    ProjectViewSet,
    basename="portfolio-projects",
)

portfolio_router.register(
    r"skills",
    SkillViewSet,
    basename="portfolio-skills",
)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', ApiRootView.as_view()),
    path('', include(router.urls)),
    path('', include(portfolio_router.urls)),
]
