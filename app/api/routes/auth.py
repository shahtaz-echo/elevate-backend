from fastapi import APIRouter, Body
from typing import List
from app.utils.api_response import APIResponse
from app.modules.auth.schema import UserInList, LoginPayloadInList, RegisterPayloadInList, CreatedNewUserInList, TokenInList
from app.modules.auth.services import create_user_service, login_service, user_details_service

router = APIRouter()

@router.post("/register", response_model=APIResponse, name="auth:register")
async def create_user(register_payload: RegisterPayloadInList) -> APIResponse:
    created_user = await create_user_service(register_payload)
    return APIResponse(
        status_code= 200,
        success=True,
        data = CreatedNewUserInList(**created_user),
        message="New User Created Successfully!"
    )

@router.post("/login", response_model=APIResponse, name="auth:login")
async def login(login_payload: LoginPayloadInList) -> APIResponse:
    token = await login_service(login_payload)
    return APIResponse(
        status_code= 200,
        success=True,
        data = TokenInList(**token),
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