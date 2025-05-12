from typing import Dict, Any, List
# from geopy.geocoders import Nominatim
# from geopy.exc import GeocoderTimedOut, GeocoderUnavailable
from pgeocode import Nominatim
from pluscodes import PlusCode
from app.config import typesense
from app.model import Product

class ProductService:
    def __init__(self):
        self.geolocator = Nominatim("br")

    def _zipcode_to_coordinates(self, zipcode: str) -> tuple[float, float]:
        try:
            location = self.geolocator.query_postal_code(zipcode)
            if location is None:
                raise ValueError(f"Could not find coordinates for zipcode: {zipcode}")
            return (location.latitude, location.longitude)
        except Exception as e:
            raise ValueError(f"Error geocoding zipcode: {str(e)}")

    def find_products_by_zipcode(self, zipcode: str) -> List[Dict[str, Any]]:
        try:
            lat, lon = self._zipcode_to_coordinates(zipcode)

            params = {
                'q': self._convert_lat_lon_to_pluscode(lat, lon),
                'query_by': 'pluscode',
            }

            return typesense.search(params)
        except Exception as e:
            raise Exception(f"Error searching products: {str(e)}")
        
    def save_product(self, product: Product):
        pluscode = self._convert_lat_lon_to_pluscode(product.lat, product.lon)
        
        document = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'pluscode': pluscode
        }
        
        typesense.save(document)

    def _convert_lat_lon_to_pluscode(self, lat: float, lon: float) -> str:
        return str(PlusCode(lat=lat, lon=lon))
        
service = ProductService()