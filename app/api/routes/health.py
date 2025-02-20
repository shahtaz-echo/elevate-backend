from fastapi import APIRouter
from app.api.dependencies.response import APIResponse
from app.core.settings import get_settings

settings = get_settings()
router = APIRouter()

@router.get("", response_model=APIResponse, name="health:get-health")
async def get_health() -> APIResponse:
    return APIResponse(
        status_code=200,
        success=True,
        data={
            "title": settings.project_name,
            "api_prefix": settings.api_prefix
        },
        message="Server is running!"
    )
