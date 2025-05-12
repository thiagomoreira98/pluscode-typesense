import random

from faker import Faker
from pluscodes import PlusCode
from app.core.model import Product
from app.config import database, settings
from app.core.typesense import Typesense

fake = Faker()

def generate_products(count: int = 10) -> list[Product]:
    typesense = Typesense(collection_name=settings.TYPESENSE_COLLECTION_NAME)

    with database.get_session() as session:
        for _ in range(count):
            # Generate realistic coordinates for Brazilian territory
            lat = round(random.uniform(-33.0, 5.0), 6) # Brazilian latitude range
            lon = round(random.uniform(-74.0, -34.0), 6) # Brazilian longitude range
            
            product = Product(
                name=fake.word().capitalize() + " " + fake.word().capitalize(),
                price=round(random.uniform(10.0, 1000.0), 2),
                lat=lat,
                lon=lon
            )

            session.add(product)

            typesense.save({
                'id': str(product.id),
                'name': product.name,
                'price': product.price,
                'lat': product.lat,
                'lon': product.lon,
                'pluscode': PlusCode(lat=product.lat, lon=product.lon).code
            })