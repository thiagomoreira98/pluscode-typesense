import urllib

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic_core import MultiHostUrl

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="allow"
    )

    LOG_LEVEL: str = "INFO"
    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_NAME: str
    DATABASE_SHOW_SQL: bool = False
    TYPESENSE_HOST: str
    TYPESENSE_PORT: int
    TYPESENSE_API_KEY: str
    TYPESENSE_COLLECTION_NAME: str

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