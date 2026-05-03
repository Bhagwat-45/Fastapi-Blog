from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DB_URL = "sqlite:///./blog.db"

#Connection to the DB
engine = create_engine(
    url=DB_URL,
    connect_args={"check_same_thread": False}
)

#Session is a transaction with a DB. Each Transaction is a session.
SessionLocal = sessionmaker(autoflush=False, autocommit=False,bind=engine)


class Base(DeclarativeBase):
    pass

def get_db():
    with SessionLocal() as db:
        yield db