from django.contrib import admin
from players.models import Player, Team, Position

# Register your models here.
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Position)
