from typing import Union
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

async def http422_error_handler(
    _: Request,
    exc: Union[RequestValidationError, ValidationError],
) -> JSONResponse:
    errors = exc.errors()
    missing_fields = [
        ". ".join(error["loc"][1:]) for error in errors if len(error["loc"]) > 1
    ]

    if len(missing_fields) > 1:
        formatted_fields = ", ".join(missing_fields[:-1]) + " and " + missing_fields[-1]
    else:
        formatted_fields = missing_fields[0] if missing_fields else "unknown field"

    # Determine message type (extra field or missing field)
    error_type = errors[0].get("type", "")
    if error_type == "extra_forbidden":
        message = f"Extra field{'s are' if len(missing_fields) > 1 else ' is'} not allowed: {formatted_fields}"
    else:
        message = f"Required field{'s are' if len(missing_fields) > 1 else ' is'} missing: {formatted_fields}"

    return JSONResponse(
        {
            "status_code": HTTP_422_UNPROCESSABLE_ENTITY,
            "success": False,
            "message": message,
        },
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
    )
