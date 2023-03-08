from enum import Enum
from typing import Optional

from fastapi import APIRouter, Depends, Response, status

from router.blog_posts import required_functionality

router = APIRouter(
    prefix="/blog",
    tags=["blog"],
)


@router.get(
    path="/all",
    summary="Fetch all blogs",
    description="This API call simulates fetching all blogs",
    response_description="the list of available blogs",
)
def get_all_blogs(
    page=1,
    page_size: Optional[int] = None,
    req_parameter: dict = Depends(required_functionality),
):
    return {"message": f"All {page_size} blogs on page {page}", "req": req_parameter}


@router.get(
    path="/{id}/comments/{comment_id}",
    tags=["comments"],
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


@router.get(
    path="/type/{type}",
)
def get_blog_type(type: BlogType):
    return {"message": f"Blog type is {type}"}


@router.get(path="/{id}", status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"blog {id} not found"}
    else:
        return {"message": f"Blog with id {id}"}
