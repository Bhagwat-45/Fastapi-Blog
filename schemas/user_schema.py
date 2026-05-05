from pydantic import BaseModel, ConfigDict, Field, EmailStr
from datetime import datetime

class UserBase(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr = Field(max_length=120)

class UserCreate(UserBase):
    pass 

class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int 
    
class UserUpdate(BaseModel):
    username: str | None = Field(default=None,min_length=3, max_length=50)
    email: EmailStr | None = Field(default=None,max_length=120)


