from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.dependencies.response import APIResponse
from app.schema.users import UserCreate, CreatedNewUserInList, LoginPayload, TokenInList
from app.modules.auth import create_user_service, login_service
from app.db.database import get_db

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
        message="New User Created Successfully!",
        data=CreatedNewUserInList(**created_user),
    )

@router.post("/login", response_model=APIResponse, name="auth:login")
async def login(login_payload: LoginPayload, db: Session = Depends(get_db)) -> APIResponse:
    token = await login_service(login_payload, db=db)
    return APIResponse(
        status_code= 200,
        success=True,
        message="User Logged In!",
        data = TokenInList(**token)
    )
