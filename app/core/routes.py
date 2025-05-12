from fastapi import APIRouter
from app.core.controller import ProductController
from app.core.model import ProductDTO

router = APIRouter()
controller = ProductController()

@router.get("/search/{zipcode}")
def index(zipcode: str):
    return controller.search(zipcode)

@router.post("/product")
def create(product: ProductDTO):
    return controller.save(product)