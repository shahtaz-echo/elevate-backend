from pydantic import BaseModel
from typing import Any, Union
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from fastapi import Request

class APIResponse(BaseModel):
    status_code: int
    success: bool
    message: str
    data: Union[dict, list, Any]

class APIError(Exception):
    def __init__(self, status_code: int, success: bool, message: str):
        self.status_code = status_code
        self.success = success
        self.message = message

async def api_error_handler(request: Request, exc: APIError):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status_code": exc.status_code,
            "success": exc.success,
            "message": exc.message
        },
    )
