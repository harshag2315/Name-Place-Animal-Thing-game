from geopy.geocoders import Nominatim

def is_place(place):
    # Create a geolocator object
    geolocator = Nominatim(user_agent="my_app")

    # Try to geocode the place
    location = geolocator.geocode(place)

    # Check if location is found
    if location is not None:
        return True
    else:
        return False
