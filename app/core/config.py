from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    app_name: str = "Secure Wallet API"
    environment: str = "development"
    debug: bool = False

    # Database connection strings
    database_host: str = "127.0.0.1"
    database_port: int = 5432

    database_name: str = Field(validation_alias="APP_DB_NAME")
    database_user: str = Field(validation_alias="APP_DB_USER")
    database_password: SecretStr = Field(validation_alias="APP_DB_PASSWORD")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()