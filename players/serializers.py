import json
from datetime import date
from rest_framework import serializers
from players.models import Player, Position, Team
from api.redis import redis_get, random_player_key


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
        fields = (
            "id",
            "first_name",
            "last_name",
            "number",
            "drafted",
            "position",
            "position_type",
            "team",
            "conference",
            "division",
        )


class RandomPlayerSerializer(PlayerSerializer):
    daily_date = serializers.SerializerMethodField()
    daily_number = serializers.SerializerMethodField()

    def get_daily_date(self, obj):
        str_data = redis_get(key=random_player_key)
        data = json.loads(str_data)
        return data["date"]

    def get_daily_number(self, obj):
        start_date = date(2023, 2, 3)
        today = date.today()
        daily_number = start_date - today
        return daily_number.days

    class Meta(PlayerSerializer.Meta):
        fields = PlayerSerializer.Meta.fields + ("daily_date", "daily_number")
