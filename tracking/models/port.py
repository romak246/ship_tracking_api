from django.db import models
from django_countries.fields import CountryField


class Port(models.Model):
    name = models.CharField('Название', max_length=20)
    code = models.CharField('Код', max_length=10, unique=True)
    latitude = models.DecimalField('Широта', max_digits=20, decimal_places=15)
    longitude = models.DecimalField('Долгота', max_digits=20, decimal_places=15)
    country = CountryField('Страна')

    def __str__(self):
        return self.name
