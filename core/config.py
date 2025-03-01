from pydantic_settings import BaseSettings
from pydantic import BaseModel


class AppConfig(BaseModel):
    APP_NAME: str = "FastAPI"
    APP_VERSION: str = "0.1"
    APP_DESCRIPTION: str = "FastAPI application"
    APP_DEBUG: bool = True

    class Config:
        env_file = ".env"

class ApiConfig(BaseModel):
    PREFIX: str = "/api"
    VERSION: str = "v1"

class RunConfig(BaseModel):
    HOST: str = "localhost"
    PORT: int = 8000
    RELOAD: bool = True

class Settings(BaseSettings):
    app: AppConfig = AppConfig()
    api: ApiConfig = ApiConfig()
    run: RunConfig = RunConfig()

settings = Settings()