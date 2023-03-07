from fastapi import FastAPI

from router import blog_get, blog_posts

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_posts.router)


@app.get("/")
def homepage():
    return {"message": "Homepage"}


@app.get("/hello")
def homepage():
    return {"message": "Hello World!"}
