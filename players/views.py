import random
from api.redis import redis_flushall, redis_get, redis_set, random_player_key
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from players.serializers import PlayerSerializer, PositionSerializer, TeamSerializer
from players.models import Player, Position, Team

# Create your views here.
class PlayerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class StoreRandomPlayerView(APIView):
    def get(self, request, format=None):
        queryset = Player.objects.all()
        random_player = random.choice(queryset)
        serializer = PlayerSerializer(random_player)
        redis_flushall()
        redis_set(key=random_player_key, value=serializer.data["id"], ex_seconds=3600 * 24)
        return Response(serializer.data)


class RetreiveRandomPlayerView(APIView):
    def get(self, request, format=None):
        random_player_id = redis_get(key=random_player_key)
        try:
            queryset = Player.objects.get(id=random_player_id)
            serializer = PlayerSerializer(queryset)
            return Response(serializer.data)
        except Player.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class PositionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
