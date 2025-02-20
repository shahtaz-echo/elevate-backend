from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException
from fastapi.exceptions import RequestValidationError

from app.core.settings import get_settings
from app.api.errors.http_error import http_error_handler
from app.api.errors.validation_error import http422_error_handler
from app.api.dependencies.response import APIError, api_error_handler

from app.api.routes.api import router as api_router
from app.db.init_db import init_db

def run_application() ->FastAPI:
    settings = get_settings()
    application = FastAPI(**settings.fastapi_kwargs)

    application.add_middleware(
        CORSMiddleware,
        allow_origins = settings.allowed_hosts, 
        allow_credentials = settings.allowed_credentials,
        allow_methods = ["*"],
        allow_headers = ["*"],
    )
 
    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_exception_handler(RequestValidationError, http422_error_handler)
    application.add_exception_handler(APIError, api_error_handler)

    application.include_router(api_router, prefix=settings.api_prefix)

    init_db()

    return application


app = run_application()