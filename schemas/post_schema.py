from pydantic import BaseModel, ConfigDict, Field, EmailStr
from datetime import datetime
from .user_schema import UserResponse

class PostBase(BaseModel):
    title: str = Field(min_length=2, max_length=100)
    content: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=50)

class PostUpdate(BaseModel):
    title : str | None = Field(default=None, min_length=1, max_length= 100)
    content : str| None = Field(default=None, min_length=1)
    

class PostCreate(PostBase):
    user_id : int # Temp


class PostResponse(PostBase):
    model_config = ConfigDict(
        from_attributes=True
    )
    #In Pydantic Model V2, Setting from_attributes=True
    id: int 
    date_posted: datetime
    author: UserResponse
    
