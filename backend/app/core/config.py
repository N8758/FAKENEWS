import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Load variables from .env file
load_dotenv()

class Settings(BaseSettings):
    """
    Application settings loaded from environment variables or .env file.
    """

    APP_NAME: str = "Fake News Detection API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # Server
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", 8000))

    # HuggingFace model
    MODEL_NAME: str = os.getenv("MODEL_NAME", "distilbert-base-uncased")
    MODEL_PATH: str = os.getenv("MODEL_PATH", "")  # optional local path

    # Security (optional future use)
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecret")
    ALLOWED_ORIGINS: str = os.getenv("ALLOWED_ORIGINS", "*")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Singleton instance
settings = Settings()
