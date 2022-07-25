
# Pydantic
from models.base.users_base_model import UserBase
from pydantic import BaseModel, EmailStr, Field

class UserRequestModel(UserBase):
    password: str = Field(..., min_length=8, max_length=40)