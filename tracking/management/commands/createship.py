import random
import string

from django.core.management import BaseCommand
from django_countries import countries

from tracking.helpers.random_location_in_water import random_location_in_water
from tracking.models.port import Port
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

    @staticmethod
    def get_random_destination():
        ports = Port.objects.all()
        return random.choice(ports)

    @staticmethod
    def generate_codename():
        letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
        digits = ''.join(str(random.randint(0, 9)) for _ in range(4))
        return f"{letters}{digits}"

    def handle(self, *args, **options):
        count = options['c']
        for i in range(count):
            cords = random_location_in_water()
            new_ship = Ship(
                code=self.generate_imo_number(),
                codename=self.generate_codename(),
                country=self.get_random_country(),
                destination=self.get_random_destination(),
                tonnage=self.generate_ship_tonnage(),
                type=self.get_random_ship_type(),
                latitude=cords[0],
                longitude=cords[1],
            )
            new_ship.image = f"static/img/{new_ship.type}.jpg"
            new_ship.save()
            print(f'Создан {new_ship.code, new_ship.country.name}')
