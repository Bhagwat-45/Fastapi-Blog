from fastapi import APIRouter,Depends, HTTPException,status, Request
from models.posts_model import Post
from schemas.post_schema import PostCreate, PostResponse
from typing import Annotated
from sqlalchemy.orm import Session
from sqlalchemy import select
from database.database import get_db

router = APIRouter(tags=["Posts"])

@router.get("/api/posts",response_model=list[PostResponse])
def get_posts(db: Annotated[Session, Depends(get_db)]):
    pass

@router.post("/api/posts",response_model=PostResponse,status_code=status.HTTP_201_CREATED)
def create_post(post: PostCreate, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(Post)


@router.get("/api/posts/{post_id}",response_model=PostResponse)
def get_post(post_id:int, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(Post).where(Post.id == post_id))
    post = result.scalars().first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with {post_id} not found.")
    
    return post

