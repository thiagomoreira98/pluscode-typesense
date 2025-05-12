from app.core.service import ProductService
from app.core.model import ProductDTO

class ProductController:
    def __init__(self):
        self.service = ProductService()

    def search(self,zipcode: str):
        return self.service.find_by_zipcode(zipcode)
    
    def save(self, product: ProductDTO):
        self.service.save(product)
        return {"message": "Product created successfully"}
    
