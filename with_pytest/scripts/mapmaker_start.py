class Point():
    def __init__(self, city, lat, long):
        if type(city) != str:
            raise ValueError("City name has to be a string.")
        if not (-90 <= lat <= 90) or not (-180 <= long <= 180):
            raise ValueError("Invalid lat/long value.")
        self.city = city
        self._lat = lat
        self._long = long

    def get_lat_long(self):
        return (self._lat, self._long)
