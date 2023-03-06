from enum import Enum
from typing import Optional

from fastapi import FastAPI, Response, status

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Homepage"}


@app.get("/hello")
def index():
    return {"message": "Hello World"}


@app.get("/blog/all")
def get_all_blogs(page=1, page_size: Optional[int] = None):
    return {"message": f"All {page_size} blogs on page {page}"}


@app.get("/blog/{id}/comments/{comment_id}")
def get_comment(
    id: int, comment_id: int, valid: bool = True, username: Optional[str] = None
):
    return {
        "message": f"blod with id {id}, comment id = {comment_id}, valid: {valid}, username is {username}"
    }


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


@app.get("/blog/type/{type}")
def get_blog_type(type: BlogType):
    return {"message": f"Blog type is {type}"}


@app.get("/blog/{id}", status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"blog {id} not found"}
    else:
        return {"message": f"Blog with id {id}"}
