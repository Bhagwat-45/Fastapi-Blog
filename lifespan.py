from fastapi import FastAPI
from database.database import Base, engine
from contextlib import asynccontextmanager
from models.posts_model import Post
from models.users_model import User

@asynccontextmanager
async def lifespan(_app: FastAPI):
    #startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    #shutdown
    await engine.dispose()