# Generated by Django 4.1.5 on 2023-02-01 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("players", "0003_alter_player_position_alter_player_team"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="abbreviation",
            field=models.CharField(default="NA", max_length=3),
        ),
    ]
