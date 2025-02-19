from fastapi import Depends, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.auth_config import get_hashed_password, verify_password
from app.services import jwt
from app.core.settings import get_settings

from app.schema.users import UserCreate, User as UserSchema, LoginPayload
from app.models.users import User as UserModel

settings = get_settings()

async def create_user_service(payload:UserCreate, db: Session = Depends(get_db)):
    existed_user = db.query(UserModel).filter(
        (UserModel.email == payload.email) | (UserModel.username == payload.username)
    ).first()

    if existed_user:
        if existed_user.email == payload.email:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail="Email is already registered"
            )
        else:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail="Username is already taken"
            )
    
    hashed_password = get_hashed_password(payload.password)
    created_user = UserModel(
        first_name=payload.first_name,
        last_name=payload.last_name,
        username=payload.username,
        email=payload.email,
        password=hashed_password,
        bio=None,
        designation=None,
        image=None
    )
    db.add(created_user)
    db.commit()
    db.refresh(created_user)

    user_data = UserSchema.model_validate(created_user, from_attributes=True)
    
    access_token = jwt.create_access_token(
        created_user,
        str(settings.jwt_access_secret),
    )
    refresh_token = jwt.create_refresh_token(
        existed_user,
        str(settings.jwt_refresh_secret),
    )

    return {
        "user": user_data,
        "access_token": access_token,
        "refresh_token": refresh_token
    }

async def login_service(payload:LoginPayload, db: Session = Depends(get_db)):
    existed_user = db.query(UserModel).filter(
        (UserModel.email == payload.userOrEmail) | (UserModel.username == payload.userOrEmail)
    ).first()

    if not existed_user:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="Username does not exist"
        )
    
    password_matched = verify_password(payload.password, existed_user.password)

    if not password_matched:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="Password is incorrect"
        )
   
    access_token = jwt.create_access_token(
        existed_user,
        str(settings.jwt_access_secret),
    )

    refresh_token = jwt.create_refresh_token(
        existed_user,
        str(settings.jwt_refresh_secret),
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }
