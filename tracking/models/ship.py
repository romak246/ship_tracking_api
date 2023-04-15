from django.db import models
from django_countries.fields import CountryField

from tracking.models.port import Port

ship_types = (
    ('container_ship', 'Контейнеровоз'),
    ('tanker', 'Танкер'),
    ('fishing', 'Рыболовное'),
    ('passenger', 'Пассажирское'),
    ('yacht', 'Яхта'),
    ('tugboat', 'Буксир'),
)


class Ship(models.Model):
    code = models.CharField('Номер ИМО', max_length=20)
    codename = models.CharField('Позывной', max_length=20, blank=True)
    image = models.ImageField('Изображение', upload_to='static/img/', blank=True)
    destination = models.ForeignKey(Port, verbose_name='Пункт назначения', related_name='ships',
                                    on_delete=models.CASCADE, null=True)
    country = CountryField('Страна')
    tonnage = models.DecimalField('Тоннаж', max_digits=10, decimal_places=2)
    type = models.CharField('Тип судана', max_length=50, choices=ship_types)
    latitude = models.DecimalField('Широта', max_digits=20, decimal_places=15)
    longitude = models.DecimalField('Долгота', max_digits=20, decimal_places=15)

    def __str__(self):
        return f"{self.code}, {self.get_type_display()} ({self.country.name})"
