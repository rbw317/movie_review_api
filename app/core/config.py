from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Values come from environment variables or a .env file (e.g. LOG_LEVEL=DEBUG)."""

    model_config = SettingsConfigDict(env_file=".env")

    app_name: str = "Search API"
    log_level: str = "INFO"


settings = Settings()