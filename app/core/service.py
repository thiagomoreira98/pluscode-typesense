from uuid import uuid4
from typing import List
from app.config import settings, logger
from app.core.model import ProductDTO, ProductDocument
from app.core.geolocator import Geolocator
from app.core.typesense import Typesense

class ProductService:
    def __init__(self):
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
            self.logger.info(f"results found: {results['found']}")

            return list(map(lambda document: ProductDocument(**document['document']), results['hits']))
        except Exception as e:
            self.logger.error(f"Error searching products: {str(e)}")
            raise e
        
    def save(self, product: ProductDTO):
        try:
            lat, lon = self.geolocator.zipcode_to_coordinates(product.zipcode)
            pluscode = self.geolocator.coordinates_to_pluscode(lat, lon)

            document = ProductDocument(
                id=str(uuid4()),
                name=product.name,
                price=product.price,
                zipcode=product.zipcode,
                lat=lat,
                lon=lon,
                pluscode=pluscode
            )
            self.typesense.save(document.model_dump())
            self.logger.info(f"Product saved -> product={document}")
        except Exception as e:
            self.logger.error(f"Error saving product on typesense: {str(e)}")
            raise e
