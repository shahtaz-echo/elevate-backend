from fastapi import APIRouter, Body, Depends
from sqlalchemy.orm import Session
from app.utils.api_response import APIResponse
from app.schema.users import UserCreate, CreatedNewUserInList, LoginPayload, TokenInList, User as UserSchema
from app.modules.auth import create_user_service, login_service
from app.db.database import get_db
from app.services.security import SecurityJWT

router = APIRouter()

@router.post("/register", response_model=APIResponse, name="auth:register")
async def create_user(
    register_payload: UserCreate,
    db: Session = Depends(get_db)
) -> APIResponse:
    created_user = await create_user_service(register_payload, db=db)
    return APIResponse(
        status_code=200,
        success=True,
        data=CreatedNewUserInList(**created_user),
        message="New User Created Successfully!"
    )

@router.post("/login", response_model=APIResponse, name="auth:login")
async def login(login_payload: LoginPayload, db: Session = Depends(get_db)) -> APIResponse:
    token = await login_service(login_payload, db=db)
    return APIResponse(
        status_code= 200,
        success=True,
        data = TokenInList(**token),
        message="User Logged In!"
    )

@router.get("/profile", response_model=APIResponse, name="auth:user-details")
async def user_details(
    user: UserSchema = Depends(SecurityJWT().get_user_from_token)
) -> APIResponse:
    return APIResponse(
        status_code=200,
        success=True,
        data=user,
        message="User Details Received!"
    )