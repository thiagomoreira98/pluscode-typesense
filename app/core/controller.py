from fastapi.responses import JSONResponse
from app.core.service import ProductService
from app.core.model import ProductDTO

class ProductController:
    def __init__(self):
        self.service = ProductService()

    def search(self,zipcode: str):
        try:
            return self.service.find_by_zipcode(zipcode)
        except Exception as e:
            return JSONResponse(status_code=500, content={"message": "Error searching products"})
    
    def save(self, product: ProductDTO):
        try:
            self.service.save(product)
            return {"message": "Product created successfully"}
        except Exception as e:
            return JSONResponse(status_code=500, content={"message": "Error creating product"})
    
