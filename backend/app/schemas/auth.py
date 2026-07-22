from pydantic import BaseModel
from pydantic import EmailStr


class LoginRequest(BaseModel):

    email: EmailStr

    password: str


class LoginResponse(BaseModel):

    access_token: str

    token_type: str = "bearer"