from fastapi import FastAPI, Request, HTTPException, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from database.database import Base, engine
from models.posts_model import Post
from models.users_model import User
from router import post_router, user_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(post_router.router)
app.include_router(user_router.router)



@app.get("/", status_code=status.HTTP_200_OK)
def home():
    return {"message": "Hello"}

