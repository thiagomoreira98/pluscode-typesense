from app.service import service

def search(zipcode: str):
    return service.find_products_by_zipcode(zipcode)
