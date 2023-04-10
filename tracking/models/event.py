import random

from datetime import timedelta, datetime
from django.db import models
from django.utils import timezone

from tracking.models.ship import Ship

event_types = (
    ('авария', 'Авария'),
    ('захват', 'Захват'),
    ('пожар', 'Пожар'),
    ('потеря', 'Потеря'),
    ('поломка', 'Поломка')
)


class Event(models.Model):
    date = models.DateTimeField(default=datetime.now)
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50, choices=event_types)
    latitude = models.DecimalField('Широта', max_digits=20, decimal_places=15, default=0)
    longitude = models.DecimalField('Долгота', max_digits=20, decimal_places=15, default=0)

    def __str__(self):
        return f"{self.event_type} {self.ship.get_type_display()}, {self.ship.code}, {self.ship.country.name}"
