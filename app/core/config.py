from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_TITLE: str = "My FastAPI App"
    APP_VERSION: str = "1.0.0"
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()
