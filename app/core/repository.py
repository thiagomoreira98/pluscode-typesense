from app.core.model import Product
from app.config import database

class ProductRepository:
    
    def save(self, product: Product) -> Product:
        with database.get_session() as session:
            session.add(product)