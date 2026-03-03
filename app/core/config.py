from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "PLATAFORMA_IOT API"
    PROJECT_VERSION: str = "1.0.0"
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    EXPIRACION_TOKEN: int = 30

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
