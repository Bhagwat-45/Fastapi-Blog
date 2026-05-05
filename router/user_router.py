from fastapi import APIRouter, Depends, HTTPException, status, Request
from schemas.user_schema import UserCreate, UserResponse, UserUpdate
from typing import Annotated
from sqlalchemy import select
from sqlalchemy.orm import Session
from models.users_model import User
from models.posts_model import Post
from database.database import get_db
from schemas.post_schema import PostResponse


router = APIRouter(prefix="/api", tags=["Users"])

@router.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(User).where(User.username == user.username))
    existing_user = result.scalars().first()
    if existing_user :
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists",

        )
    
    result = db.execute(select(User).where(User.email == user.email))
    existing_email = result.scalars().first()

    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email Address already exists"
        )
    
    new_user = User(
        username = user.username,
        email = user.email,

    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    

@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with {user_id} not found.")
    
    return user

@router.get("/users/{user_id}/posts", response_model=list[PostResponse])
def get_user_posts(user_id: int, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with {user_id} not found")
    
    result = db.execute(select(Post).where(Post.user_id==user_id))
    posts = result.scalars().all()
    return posts


@router.patch("/users/{user_id}", status_code=status.HTTP_200_OK)
def updte_user(user_id: int, user_update: UserUpdate, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with {user_id} not found."
        )
    
    if user_update.username is not None and user_update.username != user.username:
        result = db.execute(
            select(User).where(User.username == user_update.username)
        )
        existing_user = result.scalars().first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already exists."
            )
    if user_update.email is not None and user_update.email != user.email:
        result = db.execute(
            select(User).where(User.email == user_update.email)
        )
        existing_email = result.scalars().first()

        if existing_email:
            raise HTTPException(
                detail=f"User with email {existing_email} already exists",
                status_code=status.HTTP_400_BAD_REQUEST
            )
    
    if user_update.username is not None:
        user.username = user_update.username
    if user_update.email is not None:
        user.email = user_update.email
    
    db.commit()
    db.refresh(user)
    return user

@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    db.delete(user)
    db.commit()


