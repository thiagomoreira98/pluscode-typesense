from fastapi.responses import JSONResponse
from app.core.service import ProductService
from app.core.model import ProductDTO

class ProductController:
    def __init__(self):
        self.service = ProductService()

    def _validate_search_params(self, zipcode: int | None):
        if zipcode is None:
            return JSONResponse(status_code=400, content={"message": "zipcode are required"})

    def search(self, zipcode: int, radius: int):
        try:
            self._validate_search_params(zipcode)
            return self.service.find_by_radius_using_location(zipcode, radius)
        except Exception as e:
            return JSONResponse(status_code=500, content={"message": "Error searching products"})
        
    def search_using_pluscode(self, zipcode: int):
        try:
            self._validate_search_params(zipcode)
            return self.service.find_by_radius_using_pluscode(zipcode)
        except Exception as e:
            return JSONResponse(status_code=500, content={"message": "Error searching products"})
        
    def save(self, product: ProductDTO):
        try:
            self.service.save(product)
            return {"message": "Product created successfully"}
        except Exception as e:
            return JSONResponse(status_code=500, content={"message": "Error creating product"})
    
