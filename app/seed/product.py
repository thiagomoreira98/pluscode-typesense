import random
import math

from uuid import uuid4
from faker import Faker
from pluscodes import PlusCode
from pgeocode import Nominatim
from app.config import settings, logger
from app.core.typesense import Typesense
from app.core.model import ProductDocument

fake = Faker('pt_BR')
geolocator = Nominatim("br")
typesense = Typesense(collection_name=settings.TYPESENSE_COLLECTION_NAME)
logger = logger.get("app.seed.product")

def generate_products(count: int = 1000):
    logger.info(f"Generating {count} products")
   
    for n in range(count):
        try:
            # Generate realistic coordinates for Brazilian territory
            zipcode = f"{random.randint(10000, 99999)}-000"
            location = geolocator.query_postal_code(zipcode)
            
            if location is None or math.isnan(location.latitude) or math.isnan(location.longitude):
                continue

            pluscode = PlusCode(lat=location.latitude, lon=location.longitude).code

            document = ProductDocument(
                id=str(uuid4()),
                name=fake.word().capitalize() + " " + fake.word().capitalize(),
                price=round(random.uniform(10.0, 1000.0), 2),
                zipcode=zipcode,
                lat=location.latitude,
                lon=location.longitude,
                pluscode=pluscode
            )
        
            typesense.save(document)
        except Exception as e:
            pass
        finally:
            logger.debug(f"Product created: {n+1} of {count}")

    logger.info(f"Products generated successfully")
