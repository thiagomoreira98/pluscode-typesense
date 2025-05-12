import urllib

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic_core import MultiHostUrl

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    DATABASE_HOST: str = "localhost"
    DATABASE_PORT: int = 5432
    DATABASE_USER: str = "postgres"
    DATABASE_PASSWORD: str
    DATABASE_NAME: str = "products"
    DATABASE_SHOW_SQL: bool = False

    TYPESENSE_HOST: str = "localhost"
    TYPESENSE_PORT: int = 8108
    TYPESENSE_API_KEY: str
    TYPESENSE_COLLECTION_NAME: str = "products"

    @property
    def DATABASE_URL(self) -> str:
        return str(MultiHostUrl.build(
            scheme="postgresql+psycopg2",
            host=self.DATABASE_HOST,
            port=self.DATABASE_PORT,
            username=self.DATABASE_USER,
            password=urllib.parse.quote_plus(self.DATABASE_PASSWORD),
            path=self.DATABASE_NAME,
        ))

settings = Settings()