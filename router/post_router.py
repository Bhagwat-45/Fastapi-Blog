from fastapi import APIRouter,Depends, HTTPException,status, Requ
from models.posts_model import Post
from schemas.post_schema import PostCreate, PostResponse, PostUpdate
from typing import Annotated
from sqlalchemy.orm import Session
from sqlalchemy import select
from database.database import get_db
from models import User

router = APIRouter(tags=["Posts"])

@router.get("/api/posts",response_model=list[PostResponse])
def get_posts(db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(Post))
    posts = result.scalars().all()

    if not posts:
        return "No posts found"
    return posts

@router.post("/api/posts",response_model=PostResponse,status_code=status.HTTP_201_CREATED)
def create_post(post: PostCreate, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(User).where(User.id == post.user_id))
    user = result.scalars().first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with {post.user_id} doesn't exist.")
    
    new_post = Post(
        author = post.author,
        title = post.title,
        content = post.content,
        user_id = post.user_id
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

@router.get("/api/posts/{post_id}",response_model=PostResponse)
def get_post(post_id:int, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(Post).where(Post.id == post_id))
    post = result.scalars().first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with {post_id} not found.")
    
    return post


@router.put("/api/posts/{post_id}", response_model=PostResponse)
def update_post_full(post_id: int, post_data: PostCreate,db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(Post).where(Post.id == post_id))
    post = result.scalars().first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    
    if post_data.user_id != post.user_id:
        result = db.execute(select(User).where(User.id == post_data.user_id))
        user = result.scalars().first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with {post.user_id} not found")
        
    post.title = post_data.title
    post.author = post_data.author
    post.content = post_data.content
    post.user_id = post_data.user_id

    db.commit()
    db.refresh(post)

