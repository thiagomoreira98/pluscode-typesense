from app.core.repository import ProductRepository
from app.core.service import ProductService
from app.core.model import ProductDTO, Product

class ProductController:
    def __init__(self):
        self.repository = ProductRepository()
        self.service = ProductService()

    def search(self,zipcode: str):
        return self.service.find_products_by_zipcode(zipcode)
    
    def save(self, product: ProductDTO):
        lat, lon = self.service.zipcode_to_coordinates(product.zipcode)

        return self.repository.save(Product(
            name=product.name,
            price=product.price,
            lat=lat,
            lon=lon
        ))
    
