from django.urls import path, include
from players import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"players", views.PlayerViewSet, basename="Players")
router.register(r"positions", views.PositionViewSet)
router.register(r"teams", views.TeamViewSet)

urlpatterns = [
    path("players/create_random/", views.RetreiveRandomPlayerView.as_view()),
    path("", include(router.urls)),
]
