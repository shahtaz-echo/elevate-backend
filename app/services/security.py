from fastapi import Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from app.api.dependencies.response import APIError

from app.services import jwt
from app.models.users import User as UserModel
from app.schema.users import User as UserSchema 

from app.core.settings import get_settings
from app.db.database import get_db

settings = get_settings()

class SecurityJWT:
    bearer_scheme = HTTPBearer(auto_error=True)

    async def get_user_from_token(
        self,
        creds: HTTPAuthorizationCredentials = Depends(bearer_scheme),
        db: Session = Depends(get_db)
    ) -> UserSchema:
        try:
            username = jwt.get_username_from_token(
                token=creds.credentials, 
                secret_key=str(settings.jwt_access_secret)
            )
            user_model = db.query(UserModel).filter(UserModel.username == username).first()
            
            if user_model is None:
                raise APIError(
                    status_code=status.HTTP_404_NOT_FOUND,
                    success=False,
                    message="User not found",
                )
            
            return UserSchema.from_orm(user_model)
        
        except ValueError as e:
            raise APIError(
                status_code=status.HTTP_401_UNAUTHORIZED,
                success=False,
                message="JWT Token is invalid",
            )
