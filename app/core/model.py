from pydantic import BaseModel

class ProductDTO(BaseModel):
    name: str
    price: float
    zipcode: int

class ProductDocument(BaseModel):
    id: str
    name: str
    price: float
    zipcode: int
    lat: float
    lon: float
    pluscode: str
