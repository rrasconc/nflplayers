from rest_framework import serializers
from players.models import Player, Position, Team


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class PlayerSerializer(serializers.ModelSerializer):
    position = serializers.CharField(source="position.name")
    position_type = serializers.CharField(source="position.type")
    team = serializers.CharField(source="team.abbreviation")
    conference = serializers.CharField(source="team.conference")
    division = serializers.CharField(source="team.division")

    class Meta:
        model = Player
        fields = "__all__"
