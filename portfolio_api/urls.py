from django.urls import path
from .views import UserList, UrlView


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('users/', UserList.as_view()),
    path('', UrlView.as_view()),
]
