from enum import StrEnum

from pydantic_settings import BaseSettings, SettingsConfigDict


class Environment(StrEnum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TESTING = "testing"


class Settings(BaseSettings):
    ENV: Environment = Environment.DEVELOPMENT

    @property
    def DEBUG(self) -> bool:
        return self.ENV == Environment.DEVELOPMENT

    PROJECT_NAME: str = "Pollaris"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"

    DATABASE_URL: str = "sqlite:///./test.db"

    model_config = SettingsConfigDict(
        env_file=".env", case_sensitive=True, extra="ignore"
    )


settings = Settings()
