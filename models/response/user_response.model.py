# Pydantic
from models.base.users_base_model import UserBase

#Pydantic
from pydantic import BaseModel, EmailStr, Field

class UserRequestModel(UserBase):
    pass 