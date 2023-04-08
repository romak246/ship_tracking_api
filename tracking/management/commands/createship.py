import random

from django.core.management import BaseCommand

from django_countries import countries
from geopy.point import Point
from geopy import distance
from random import uniform

from tracking.models.ship import ship_types, Ship


class Command(BaseCommand):
    help = 'Генерирует случайное судно'

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
    def random_location_in_water():
        """
        Функция возвращает случайные координаты, находящиеся в море.
        """
        while True:
            # генерируем случайные координаты широты и долготы
            lat = uniform(-90, 90)
            lon = uniform(-180, 180)
            # создаем объект Point с этими координатами
            point = Point(lat, lon)
            # вычисляем расстояние до ближайшей суши
            dist = distance.distance(point, Point(0, 0)).meters
            # если расстояние больше 100 км, то возвращаем координаты
            match dist:
                case dist if dist > 200000:
                    return lat, lon

    def handle(self, *args, **kwargs):
        cords = self.random_location_in_water()
        new_ship = Ship(
            code=self.generate_imo_number(),
            country=self.get_random_country(),
            tonnage=self.generate_ship_tonnage(),
            type=self.get_random_ship_type(),
            latitude=cords[0],
            longitude=cords[1],
        )
        new_ship.save()
