from fastapi import APIRouter, Query
from app.core.controller import ProductController
from app.core.model import ProductDTO

router = APIRouter()
controller = ProductController()

@router.get("/search-using-radius")
def search(
    zipcode: str = Query(None),
    radius: int = Query(default=10),
):
    return controller.search(zipcode, radius)

@router.get("/search-using-pluscode")
def search_by_pluscode(
    zipcode: str = Query(None),
):
    return controller.search_using_pluscode(zipcode)

@router.post("/product")
def create(product: ProductDTO):
    return controller.save(product)