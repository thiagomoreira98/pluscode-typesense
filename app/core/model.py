from sqlmodel import SQLModel, Field
from pydantic import BaseModel

class ProductDTO(BaseModel):
    id: int
    name: str
    price: float
    zipcode: int

class Product(SQLModel, table=True):
    __tablename__ = "products"

    id: int = Field(default=None, primary_key=True)
    name: str
    price: float
    lat: float
    lon: float