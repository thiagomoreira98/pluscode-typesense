import math

from pgeocode import Nominatim
from pluscodes import PlusCode
from app.config import logger

class Geolocator:
    def __init__(self):
        self.geolocator = Nominatim("br")
        self.logger = logger.get("app.core.geolocator")

    def zipcode_to_coordinates(self, zipcode: int) -> tuple[float, float]:
        try:
            zipcode = str(zipcode)[0:5] + "-000"
            location = self.geolocator.query_postal_code(zipcode)
            self.logger.info(f"Location: {location}")
            
            if location is None or math.isnan(location.latitude) or math.isnan(location.longitude):
                raise ValueError(f"Could not find coordinates for zipcode={zipcode}")
            
            return (location.latitude, location.longitude)
        except Exception as e:
            self.logger.error(f"Error converting zipcode to coordinates: {str(e)}")
            raise e
        
    def coordinates_to_pluscode(self, lat: float, lon: float) -> str:
        try:
            return PlusCode(lat=lat, lon=lon).code
        except Exception as e:
            self.logger.error(f"Error converting coordinates to pluscode: {str(e)}")
            raise e
