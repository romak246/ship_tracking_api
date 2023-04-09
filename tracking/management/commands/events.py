import random

from datetime import datetime, timedelta
from django.core.management import BaseCommand
from random import choice

from tracking.models.event import event_types, Event
from tracking.models.ship import Ship


class Command(BaseCommand):
    help = 'Генерирует случайное событие, принимает аргумент --c, где --c является количеством генераций событий'

    def add_arguments(self, parser):
        parser.add_argument('--c', type=int, default=1, help='Количество событий')

    @staticmethod
    def random_date(start_year=2015):
        """
        Генерирует случайную дату и время в заданном интервале.
        """
        now = datetime.now()
        start = datetime(start_year, 1, 1, 0, 0, 0)
        end = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)

        delta = end - start
        int_delta = delta.days * 24 * 60 * 60 + delta.seconds

        random_second = random.randrange(int_delta)
        random_datetime = start + timedelta(seconds=random_second)

        return random_datetime

    def handle(self, *args, **options):
        count = options['c']

        for i in range(count):
            new_event = Event(
                ship=Ship.objects.order_by('?').first(),
                event_type=choice(event_types)[0],
                date=self.random_date()

            )
            new_event.save()
