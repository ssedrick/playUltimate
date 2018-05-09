from django.db import models
from django.conf import settings

from enum import Enum


class DayOfWeek(Enum):
    MON = "Monday"
    TUE = "Tuesday"
    WED = "Wednesday"
    THU = "Thursday"
    FRI = "Friday"
    SAT = "Saturday"
    SUN = "Sunday"


class Game(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class GameDay(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    day_of_week = models.CharField(
        max_length=3,
        choices=[(day.name, day.value) for day in DayOfWeek]
    )
    attendees = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    anonymous_attendees = models.IntegerField(default=0)
    start_time = models.TimeField()
    duration = models.DurationField()

    def __str__(self):
        return "{0} on {1}".format(self.game.name, self.day_of_week)
