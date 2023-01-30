from django.urls import path, include
from players import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"players", views.PlayerViewSet)
router.register(r"positions", views.PositionViewSet)
router.register(r"teams", views.TeamViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
