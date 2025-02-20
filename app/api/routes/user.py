from fastapi import APIRouter, Depends
from app.api.dependencies.response import APIResponse
from app.schema.users import User as UserSchema
from app.services.security import SecurityJWT

router = APIRouter()

@router.get("/profile", response_model=APIResponse, name="user:profile")
async def user_details(
    user: UserSchema = Depends(SecurityJWT().get_user_from_token)
) -> APIResponse:
    return APIResponse(
        status_code=200,
        success=True,
        message="User Details Received!",
        data=user
    )