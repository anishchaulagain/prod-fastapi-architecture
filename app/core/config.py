from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "AI Brand Fedility",
    APP_VERSION: str = "1.0.0",
    DEBUG: bool = false

    # DB PART
    DB_HOST: str,
    DB_PORT: int,
    DB_USER: str,
    DB_PASSWORD: str,
    DB_NAME: str 

    #JWT PART

    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

