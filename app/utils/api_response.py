from pydantic import BaseModel
from typing import Any, Union

class APIResponse(BaseModel):
    status_code: int
    success: bool
    data: Union[dict, list, Any]
    message: str
