from typing import List, Dict, Any
from pydantic import PostgresDsn, SecretStr
from pydantic_settings import BaseSettings

from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    project_name: str = "FastAPI App"
    debug: bool = False
    allowed_hosts: List[str] = ["*"]
    allowed_credentials: bool = True
    openapi_prefix: str = ""
    api_prefix: str = "/api/v1"

    database_url: PostgresDsn
    max_connection_count: int = 10
    min_connection_count: int = 10

    jwt_access_secret: SecretStr
    jwt_refresh_secret: SecretStr
    
    jwt_token_prefix: str = "Bearer"

    class Config:
        validate_assignment = True

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            "title": self.project_name,
            "debug": self.debug,
            "openapi_prefix": self.openapi_prefix,
        }

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

def get_settings() -> Settings:
    return Settings()
