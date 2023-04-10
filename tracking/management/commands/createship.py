import random

from django.core.management import BaseCommand
from django_countries import countries

from tracking.helpers.random_location_in_water import random_location_in_water
from tracking.models.ship import ship_types, Ship


class Command(BaseCommand):
    help = 'Генерирует случайное судно, принимает аргумент --c, где --c является количеством генераций судов'

    def add_arguments(self, parser):
        parser.add_argument('--c', type=int, default=1, help='Количество генераций')
        parser.add_argument('--e', type=int, default=0, help='Количество событий')

    @staticmethod
    def get_random_country():
        return random.choice(list(countries))

    @staticmethod
    def get_random_ship_type():
        return random.choice(ship_types)[0]

    @staticmethod
    def generate_imo_number():
        return str(random.randint(1000000, 9999999))

    @staticmethod
    def generate_ship_tonnage():
        return random.randint(1000, 100000)

    def handle(self, *args, **options):
        count = options['c']
        for i in range(count):
            cords = random_location_in_water()
            new_ship = Ship(
                code=self.generate_imo_number(),
                country=self.get_random_country(),
                tonnage=self.generate_ship_tonnage(),
                type=self.get_random_ship_type(),
                latitude=cords[0],
                longitude=cords[1],
            )
            new_ship.save()
            print(f'Создан {new_ship.code, new_ship.country.name}')
