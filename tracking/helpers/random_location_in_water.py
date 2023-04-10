from django_countries import countries
from geopy.point import Point
from geopy import distance, Nominatim
from random import uniform

from tracking.helpers.get_location_type import get_location_type


def random_location_in_water():
    """
    Функция возвращает случайные координаты, находящиеся в море.
    """
    while True:
        # генерируем случайные координаты широты и долготы
        lat = uniform(-60, 90)
        lon = uniform(-180, 180)
        is_land = get_location_type(round(lat, 3), round(lon, 3))
        # создаем объект Point с этими координатами
        point = Point(lat, lon)
        # вычисляем расстояние до ближайшей суши
        dist = distance.distance(point, Point(0, 0)).kilometers
        # если расстояние больше 200 км, то возвращаем координаты
        match dist:
            case dist if dist > 200 and not is_land:
                return lat, lon
