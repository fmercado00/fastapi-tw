# Python
from datetime import date, datetime
from email.policy import default
from typing import Optional
from uuid import UUID
from models.base.users_base_model import UserBase

# Pydantic
from pydantic import BaseModel, EmailStr, Field

class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(..., min_lenght=2, max_length=256)
    created_at: datetime = Field(..., deault=datetime.now())
    updated_at: Optional[datetime] = Field(..., deault=None)
    by: UserBase = Field(...)
