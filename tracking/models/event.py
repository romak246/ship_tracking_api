from django.db import models
from tracking.models.ship import Ship


class Event(models.Model):
    EVENT_TYPES = (
        ('авария', 'Авария'),
        ('захват', 'Захват'),
        ('пожар', 'Пожар'),
        ('потеря', 'Потеря'),
        ('поломка', 'Поломка')
    )
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)
