
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    ACCESS_TOKEN_EXPIRE_MINUTES: int
    ADMIN_PASSWORD: str
    ADMIN_USERNAME: str
    ALGORITHM: str
    DATABASE_URL: str
    EMAIL_SENDER_PASSWORD: str
    SECRET_KEY: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )

secrets = Settings()
