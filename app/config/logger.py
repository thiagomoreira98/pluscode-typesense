import logging
from app.config.settings import settings

logging.basicConfig(
    level=settings.LOG_LEVEL,
    format="[%(levelname)s] - %(asctime)s - %(name)s - %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

def get(name: str):
    return logging.getLogger(name)
