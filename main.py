from fastapi import FastAPI,status
from lifespan import lifespan
from router import post_router, user_router

app = FastAPI(lifespan=lifespan)
app.include_router(post_router.router)
app.include_router(user_router.router)

@app.get("/", status_code=status.HTTP_200_OK)
def home():
    return {"message": "Hello"}

