import app.config.logger as logger

from .settings import settings
from .database.database import database
from .database.seed.product import generate_products

def init():
    database.init()
    generate_products(1000)

__all__ = ["logger", "settings", "database"]