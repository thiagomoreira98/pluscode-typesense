from pgeocode import Nominatim
from pluscodes import PlusCode

class Geolocator:
    def __init__(self):
        self.geolocator = Nominatim("br")

    def zipcode_to_coordinates(self, zipcode: str) -> tuple[float, float]:
        try:
            location = self.geolocator.query_postal_code(zipcode)
            if location is None:
                raise ValueError(f"Could not find coordinates for zipcode: {zipcode}")
            return (location.latitude, location.longitude)
        except Exception as e:
            raise ValueError(f"Error geocoding zipcode: {str(e)}")
        
    def coordinates_to_pluscode(self, lat: float, lon: float) -> str:
        return str(PlusCode(lat=lat, lon=lon))
