from geopy import Nominatim


def get_location_type(lat, lon):
    geolocator = Nominatim(user_agent="location_tracker")
    location = geolocator.reverse(f"{lat}, {lon}", exactly_one=True, addressdetails=True)
    return location
