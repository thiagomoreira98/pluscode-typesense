from typing import Dict, Any, List
from app.config import settings
from app.core.model import ProductDTO, Product
from app.core.repository import ProductRepository
from app.core.geolocator import Geolocator
from app.core.typesense import Typesense

class ProductService:
    def __init__(self):
        self.repository = ProductRepository()
        self.geolocator = Geolocator()
        self.typesense = Typesense(collection_name=settings.TYPESENSE_COLLECTION_NAME)

    def find_by_zipcode(self, zipcode: str) -> List[Dict[str, Any]]:
        try:
            lat, lon = self.geolocator.zipcode_to_coordinates(zipcode)

            params = {
                'q': self._convert_lat_lon_to_pluscode(lat, lon),
                'query_by': 'pluscode',
            }

            return self.typesense.search(params)
        except Exception as e:
            raise Exception(f"Error searching products: {str(e)}")
        
    def save(self, dto: ProductDTO):
        try:
            lat, lon = self.geolocator.zipcode_to_coordinates(dto.zipcode)

            product = self.repository.save(Product(
                name=dto.name,
                price=dto.price,
                lat=lat,
                lon=lon
            ))
        
            self.typesense.save({
                'id': str(product.id),
                'name': product.name,
                'price': product.price,
                'pluscode': self.geolocator.coordinates_to_pluscode(lat, lon)
            })
        except Exception as e:
            raise Exception(f"Error saving product: {str(e)}")
