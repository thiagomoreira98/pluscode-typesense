from typing import Dict, Any, List
from app.config import settings, logger
from app.core.model import ProductDTO, Product, ProductDocument
from app.core.repository import ProductRepository
from app.core.geolocator import Geolocator
from app.core.typesense import Typesense

class ProductService:
    def __init__(self):
        self.repository = ProductRepository()
        self.geolocator = Geolocator()
        self.typesense = Typesense(collection_name=settings.TYPESENSE_COLLECTION_NAME)
        self.logger = logger.get("app.core.service")

    def find_by_zipcode(self, zipcode: str) -> List[ProductDocument]:
        try:
            self.logger.info(f"Searching for products by zipcode: {zipcode}")
            lat, lon = self.geolocator.zipcode_to_coordinates(zipcode)
            pluscode = self.geolocator.coordinates_to_pluscode(lat, lon)
            self.logger.info(f"Pluscode: {pluscode}")

            results = self.typesense.search({
                'q': pluscode,
                'query_by': 'pluscode',
            })
            self.logger.info(f"Results found: {results['found']}")

            return list(map(lambda document: ProductDocument(**document['document']), results['hits']))
        except Exception as e:
            raise Exception(f"Error searching products: {str(e)}")
        
    def save(self, dto: ProductDTO):
        try:
            self.logger.info(f"Saving product located in zipcode={dto.zipcode}")
            lat, lon = self.geolocator.zipcode_to_coordinates(dto.zipcode)

            product = self.repository.save(Product(
                name=dto.name,
                price=dto.price,
                lat=lat,
                lon=lon
            ))
            self.logger.info(f"Product created on database: product_id={product.id}")

            pluscode = self.geolocator.coordinates_to_pluscode(lat, lon)
        
            self.typesense.save({
                'id': str(product.id),
                'name': product.name,
                'price': product.price,
                'lat': product.lat,
                'lon': product.lon,
                'pluscode': pluscode
            })
            self.logger.info(f"Product saved on typesense: pluscode={pluscode}")
        except Exception as e:
            raise Exception(f"Error saving product: {str(e)}")
