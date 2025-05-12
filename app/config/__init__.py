from .settings import settings
from .database.database import database
from .database.seed.product import generate_products

def init():
    database.init()
    generate_products(100)

__all__ = ["settings", "database"]