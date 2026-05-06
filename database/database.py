from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

DB_URL = "sqlite+aiosqlite:///./blog.db"


#Connection to the DB
engine = create_async_engine(
    url=DB_URL,
    connect_args={"check_same_thread": False}
)

#Session is a transaction with a DB. Each Transaction is a session.
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass

async def get_db():
    async with AsyncSessionLocal() as db:
        yield db