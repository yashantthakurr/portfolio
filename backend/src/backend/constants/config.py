
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):

    ACCESS_TOKEN_EXPIRE_MINUTES: int
    ADMIN_PASSWORD: str
    ADMIN_USERNAME: str
    ALGORITHM: str
    DATABASE_URL: str
    EMAIL_SENDER_PASSWORD: str
    SECRET_KEY: str
    ALLOWED_HOSTS: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )

secrets = Settings()
ALLOWED_HOSTS: List[str] = os.environ["ALLOWED_HOSTS"].split(",")
