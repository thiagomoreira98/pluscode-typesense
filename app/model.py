from sqlmodel import SQLModel, Field

class Product(SQLModel, table=True):
    __tablename__ = "products"

    id: int = Field(default=None, primary_key=True)
    name: str
    price: float
    lat: float
    lon: float