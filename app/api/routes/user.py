from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.modules.user import update_user_service
from app.api.dependencies.response import APIResponse
from app.schema.users import User as UserSchema, UserUpdateInPayload
from app.services.security import SecurityJWT
from app.models.users import User as UserModel

router = APIRouter()

@router.get("/profile", response_model=APIResponse, name="user:profile")
async def user_details(
    user: UserModel = Depends(SecurityJWT().get_user_from_token)
) -> APIResponse:
    user_data = UserSchema.from_orm(user)
    return APIResponse(
        status_code=200,
        success=True,
        message="User Details Received!",
        data=user_data
    )

@router.patch("/update", response_model=APIResponse, name="user:update")
async def user_details(
    update_payload: UserUpdateInPayload,
    current_user: UserModel = Depends(SecurityJWT().get_user_from_token),
    db: Session = Depends(get_db)
) -> APIResponse:
    updated_user = await update_user_service(update_payload, user=current_user, db=db)
    return APIResponse(
        status_code=200,
        success=True,
        message="User updated successfully!",
        data=updated_user
    )