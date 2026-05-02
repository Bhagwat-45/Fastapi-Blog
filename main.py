from fastapi import FastAPI
from fastapi.responses import HTMLResponse

posts: list[dict] = [
    {
        "id" : 1,
        "author" : "Chinmay Bhagwat",
        "title" : "FastAPI is awesome",
        "content" : "This framework is really easy to use and super fast",
        "date_posted" : "April 20, 2025",
    },
    {
        "id" : 2,
        "author" : "Chetan Bhagwat",
        "title" : "Go is great for Backend",
        "content" : "Go is fast and it has good documents",
        "date_posted" : "April 28, 2025",
    }
]

app = FastAPI()

@app.get("/",response_class=HTMLResponse,include_in_schema=False)
@app.get("/posts",response_class=HTMLResponse,include_in_schema=False)
def home():
    return f"<h1>{posts[0]['title']}</h1>"


@app.get("/api/posts")
def get_posts():
    return posts
