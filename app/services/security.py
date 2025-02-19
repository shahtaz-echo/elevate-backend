from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.services import jwt
from app.models.users import User as UserModel
from app.schema.users import User as UserSchema 

from app.db.database import get_db

from app.core.settings import get_settings

settings = get_settings()

class SecurityJWT:
    bearer_scheme = HTTPBearer(auto_error=True)

    async def get_user_from_token(
        self,
        creds: HTTPAuthorizationCredentials = Depends(bearer_scheme),
        db: Session = Depends(get_db)
    ) -> UserSchema:
        try:
            username = jwt.get_username_from_token(token=creds.credentials, secret_key=str(settings.jwt_access_secret))
            user_model = db.query(UserModel).filter(UserModel.username == username).first()
            if user_model is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
            return UserSchema.from_orm(user_model)  # Convert to UserSchema
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=str(e),
                headers={"WWW-Authenticate": "Bearer"},
            )
