# Python
from datetime import date
from email.policy import default
from typing import Optional
from uuid import UUID

# Pydantic
from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    user_id: UUID = Field(...)
    username: str = Field(...)
    email: EmailStr = Field(...)
    full_name: str = Field(..., min_length=2, max_length=150)
    birth_date: Optional[date] = Field(default=None)
