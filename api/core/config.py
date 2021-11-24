import os
from functools import lru_cache

from pydantic import BaseSettings, PostgresDsn


class Config(BaseSettings):
    # inspired from https://github.com/tiangolo/fastapi/issues/508#issuecomment-532360198

    DEBUG: bool = True
    project_name: str = "Instrumentation"
    project_description: str = "Instrumentation proof of concept"
    api_v1_route: str = "/api/v1"
    openapi_route: str = "/api/v1/openapi.json"
    HONEYCOMB_API_KEY: str = os.getenv("HONEYCOMB_API_KEY")
    HONEYCOMB_DATASET: str = "afinidata"

    DB_URI: PostgresDsn = os.getenv("DB_URI")


@lru_cache()
def get_settings() -> Config:
    return Config()
