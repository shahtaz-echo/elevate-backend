from fastapi import APIRouter
from app.utils.api_response import APIResponse
from app.modules.tags.schema import TagsInList
from app.modules.tags.services import get_tags_service

router = APIRouter()

@router.get("", response_model=APIResponse, name="tags:get-all")
async def get_tags() -> APIResponse:
    tags = await get_tags_service()
    return APIResponse(
        status_code=200,
        success=True,
        data=TagsInList(tags=tags),
        message="Tags retrieved successfully."
    )
