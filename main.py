from fastapi import FastAPI

from db import models
from db.database import engine
from router import article, blog_get, blog_posts, user

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_posts.router)
app.include_router(user.router)
app.include_router(article.router)


@app.get("/")
def homepage():
    return {"message": "Homepage"}


@app.get("/hello")
def homepage():
    return {"message": "Hello World!"}


models.Base.metadata.create_all(engine)
