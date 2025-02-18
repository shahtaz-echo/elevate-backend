from typing import List
from fastapi import APIRouter
from app.utils.api_response import APIResponse
from app.modules.auth.schema import UserInList, TokenInList
from app.modules.auth.services import create_user_service, login_service, user_details_service

router = APIRouter()

@router.post("/register", response_model=APIResponse, name="auth:register")
async def create_user() -> APIResponse:
    created_user = await create_user_service()
    return APIResponse(
        status_code= 200,
        success=True,
        data = List(user=UserInList(created_user)),
        message="New User Created Successfully!"
    )

@router.post("/login", response_model=APIResponse, name="auth:login")
async def login() -> APIResponse:
    token = await login_service()
    return APIResponse(
        status_code= 200,
        success=True,
        data = TokenInList(token),
        message="User Logged In!"
    )

@router.get("/profile", response_model=APIResponse, name="auth:user-details")
async def user_details() -> APIResponse:
    user_data = await user_details_service()
    return APIResponse(
        status_code= 200,
        success=True,
        data = UserInList(user_data),
        message="User Details Recieved!"
    )