from pydantic import BaseModel

class UserInList(BaseModel):
    first_name: str
    last_name: str
    email: str
    bio: str
    image: str
    designation: str

class TokenInList(BaseModel):
    access_token: str
    refresh_token: str

class LoginPayloadInList(BaseModel):
    email: str
    password: str

class RegisterPayloadInList(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
class CreatedNewUserInList(BaseModel):
    user: UserInList
    access_token: str
    refresh_token: str
