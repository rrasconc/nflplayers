from django.db import models


class Position(models.Model):
    OFFENSIVE = "OFF"
    DEFENSE = "DEF"
    SPECIAL_TEAMS = "ST"
    POSITION_TYPES = [(OFFENSIVE, "Offense"), (DEFENSE, "Defense"), (SPECIAL_TEAMS, "Special Teams")]

    name = models.CharField(max_length=2)
    type = models.CharField(max_length=3, choices=POSITION_TYPES)

    def __str__(self):
        return f"({self.pk}) {self.name}"


class Team(models.Model):
    AFC = "AFC"
    NFC = "NFC"
    NORTH = "NORTH"
    SOUTH = "SOUTH"
    EAST = "EAST"
    WEST = "WEST"

    CONFERENCES = [(AFC, "AFC"), (NFC, "NFC")]
    DIVISIONS = [(NORTH, "North"), (SOUTH, "South"), (EAST, "East"), (WEST, "West")]

    name = models.CharField(max_length=30)
    conference = models.CharField(max_length=3, choices=CONFERENCES)
    division = models.CharField(max_length=5, choices=DIVISIONS)
    abbreviation = models.CharField(max_length=3, default="NA")

    def __str__(self):
        return f"({self.pk}) {self.name}"


# Create your models here.
class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f"({self.pk}) {self.first_name} {self.last_name}"
