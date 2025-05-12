from fastapi import APIRouter, Query
from app.controller import search

router = APIRouter()

@router.get("/search/{zipcode}")
def index(zipcode: str):
    return search(zipcode)