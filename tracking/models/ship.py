from django.db import models
from django_countries.fields import CountryField


ship_types = (
    ('container_ship', 'Контейнеровоз'),
    ('bulk_carrier', 'Сухогруз'),
    ('oil_tanker', 'Нефтяной танкер'),
    ('gas_carrier', 'Газовоз'),
    ('chemical_tanker', 'Химический танкер'),
    ('reefer_ship', 'Рефрижераторное судно'),
    ('cruise_ship', 'Круизный лайнер'),
    ('ferry', 'Паром'),
    ('yacht', 'Яхта'),
    ('tugboat', 'Буксир'),
)


class Ship(models.Model):
    code = models.CharField('Номер ИМО', max_length=20)
    country = CountryField('Страна')
    tonnage = models.DecimalField('Тоннаж', max_digits=10, decimal_places=2)
    type = models.CharField('Тип судана', max_length=50, choices=ship_types)
    latitude = models.DecimalField('Широта',  max_digits=20, decimal_places=15)
    longitude = models.DecimalField('Долгота',  max_digits=20, decimal_places=15)

    def __str__(self):
        return f"{self.code}, {self.get_type_display()} ({self.country.name})"
