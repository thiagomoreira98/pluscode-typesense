from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="allow"
    )

    LOG_LEVEL: str = "INFO"
    TYPESENSE_HOST: str
    TYPESENSE_PORT: int
    TYPESENSE_API_KEY: str
    TYPESENSE_COLLECTION_NAME: str

settings = Settings()