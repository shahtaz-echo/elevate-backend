from pydantic_settings import BaseSettings
from typing import List, Dict, Any
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    project_name: str = "FastAPI App"
    debug: bool = False
    allowed_hosts: List[str] = ["*"]
    allowed_credentials: bool = True
    openapi_prefix: str = ""
    api_prefix: str = "/api/v1"

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
