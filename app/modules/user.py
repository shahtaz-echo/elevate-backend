from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schema.users import UserUpdateInPayload, User as UserSchema

async def update_user_service(payload: UserUpdateInPayload, user: UserSchema, db: Session):
    update_data = payload.dict(exclude_unset=True)

    for field, value in update_data.items():
        setattr(user, field, value)

    db.commit()
    db.refresh(user)

    return UserSchema.model_validate(user, from_attributes=True)