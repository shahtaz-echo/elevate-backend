from typing import Dict
from fastapi import HTTPException, Depends
from starlette.status import HTTP_400_BAD_REQUEST

from app.modules.auth.schema import LoginPayloadInList, RegisterPayloadInList
from app.services.repository.user import UsersRepository
from app.services.database import get_repository
from app.services.authentication import check_email_is_taken

from app.core.settings import get_settings as settings
from app.services.jwt import jwt

async def create_user_service(payload:RegisterPayloadInList):
    print(payload)
    users_repo: UsersRepository = Depends(get_repository(UsersRepository)),
    
    if await check_email_is_taken(users_repo, payload.email):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="email is taken",
        )
    
    user = await users_repo.create_user(**payload.dict())
    access_token = jwt.create_access_token_for_user(
        user,
        str(settings.secret_key.get_secret_value()),
    )
    refresh_token = "refresh_test"
    return {user, access_token, refresh_token}

async def login_service(payload:LoginPayloadInList):
    wrong_login_error = HTTPException(
        status_code=HTTP_400_BAD_REQUEST,
        detail="Incorrect login input",
    )
    try:
        users_repo: UsersRepository = Depends(get_repository(UsersRepository)),
        user = await users_repo.get_user_by_email(email=payload.email)
    except:
        raise wrong_login_error
    
    token = jwt.create_access_token_for_user(
        user,
        str(settings.secret_key.get_secret_value()),
    )
    return token
    

async def user_details_service():
    return {}

async def refresh_token_service():
    return {}

