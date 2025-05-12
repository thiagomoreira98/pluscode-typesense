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

def _get_coordinates(zipcode: str):
    zipcode = str(zipcode)[0:5] + "-000"
    location = geolocator.query_postal_code(zipcode)
    return (location.latitude, location.longitude)

def generate_products(count: int = 1000):
    logger.info(f"Generating {count} products")
   
    for n in range(count):
        try:
            # Generate realistic coordinates for Brazilian territory
            zipcode = f"{random.randint(10000, 99999)}-{random.randint(0, 999)}"
            # zipcode = "14400-470"
            lat, lon = _get_coordinates(zipcode)
            pluscode = PlusCode(lat=lat, lon=lon).code

            document = ProductDocument(
                id=str(uuid4()),
                name=fake.word().capitalize() + " " + fake.word().capitalize(),
                price=round(random.uniform(10.0, 1000.0), 2),
                zipcode=int(zipcode.replace("-", "")),
                lat=lat,
                lon=lon,
                pluscode=pluscode
            )
        
            typesense.save(document.model_dump())
        except Exception as e:
            logger.error(f"Error generating product: {str(e)}")
            pass
        finally:
            logger.debug(f"Product created: {n+1} of {count}")

    logger.info(f"Products generated successfully")
