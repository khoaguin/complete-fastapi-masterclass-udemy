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


@app.get(
    path="/blog/all",
    tags=["blogs"],
    summary="Fetch all blogs",
    description="This API call simulates fetching all blogs",
    response_description="the list of available blogs",
)
def get_all_blogs(page=1, page_size: Optional[int] = None):
    return {"message": f"All {page_size} blogs on page {page}"}


@app.get(
    path="/blog/{id}/comments/{comment_id}",
    tags=["blogs", "comments"],
)
def get_comment(
    id: int, comment_id: int, valid: bool = True, username: Optional[str] = None
):
    """
    Simulate fetching a comment for a blog post

    - **id**: mandatory path parameter
    - **comment_id**: mandatory path parameter
    - **valid**: optional path parameter
    - **username**: optional path parameter
    """
    return {
        "message": f"blod with id {id}, comment id = {comment_id}, valid: {valid}, username is {username}"
    }


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


@app.get(
    path="/blog/type/{type}",
    tags=["blogs"],
)
def get_blog_type(type: BlogType):
    return {"message": f"Blog type is {type}"}


@app.get(path="/blog/{id}", tags=["blogs"], status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"blog {id} not found"}
    else:
        return {"message": f"Blog with id {id}"}
