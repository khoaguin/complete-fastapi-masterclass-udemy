from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, PlainTextResponse

from auth import authentication
from db import models
from db.database import engine
from exceptions import StoryException
from router import article, blog_get, blog_posts, file, product, user

app = FastAPI()
app.include_router(file.router)
app.include_router(authentication.router)
app.include_router(blog_get.router)
app.include_router(blog_posts.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)


@app.get("/")
def homepage():
    return {"message": "Homepage"}


@app.get("/hello")
def homepage():
    return {"message": "Hello World!"}


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(status_code=418, content={"detail": exc.name})


models.Base.metadata.create_all(engine)


origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
