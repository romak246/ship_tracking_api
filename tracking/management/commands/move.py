import random
import time
from django.core.management.base import BaseCommand
from geopy import Point, distance

from tracking.helpers.get_location_type import get_location_type
from tracking.models.ship import Ship


class Command(BaseCommand):
    help = 'Все корабли передвигаются на 20 км'

    def handle(self, *args, **options):
        while True:
            for ship in Ship.objects.all():
                current_location = Point(ship.latitude, ship.longitude)
                bearing = random.uniform(0, 360)
                new_location = distance.distance(kilometers=20).destination(current_location, bearing)
                is_land = get_location_type(new_location.latitude, new_location.longitude)
                while is_land is not None:
                    is_land = get_location_type(new_location.latitude, new_location.longitude)
                ship.latitude = new_location.latitude
                ship.longitude = new_location.longitude
                ship.save()

            self.stdout.write(self.style.SUCCESS('Все корабли передвинулись на 20 км.'))
