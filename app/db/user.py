from typing import Optional

from app.db.helpers.common import DateTimeModelMixin, IDModelMixin
from app.db.helpers.rwmodel import RWModel
from app.services import security

class User(RWModel):
    first_name: str
    last_name: str
    email: str
    password: str
    username: Optional[str] = None
    bio: Optional[str] = None
    designation: Optional[str] = None
    image: Optional[str] = None

class UserInDB(IDModelMixin, DateTimeModelMixin, User):
    salt: str = ""
    hashed_password: str = ""

    def check_password(self, password: str) -> bool:
        return security.verify_password(self.salt + password, self.hashed_password)

    def change_password(self, password: str) -> None:
        self.salt = security.generate_salt()
        self.hashed_password = security.get_password_hash(self.salt + password)
