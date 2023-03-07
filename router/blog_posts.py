from typing import Dict, List, Optional

from fastapi import APIRouter, Body, Path, Query
from pydantic import BaseModel

router = APIRouter(prefix="/blog", tags=["blog"])


class Image(BaseModel):
    url: str
    alias: str


class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, str] = {"key1": "val1"}
    image: Optional[Image] = None


@router.post("/new/{id}")
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {"id": id, "data": blog, "version": version}


@router.post("/new/{id}/comment/{comment_id}")
def create_comment(
    blog: BlogModel,
    id: int,
    comment_title: int = Query(
        None,
        title="Id of the component",
        description="Some description for comment_id",
        alias="comment id",
    ),
    content: str = Body(
        ...,
        min_length=10,  # minimum length requirements
        max_length=50,  # maximum length requirements
        regex="^[a-z\s]*$",  # regrex validation
    ),
    v: Optional[List[str]] = Query(["1.0", "1.1", "1.2"]),
    comment_id: int = Path(None, gt=5, le=10),
):
    return {
        "blog": blog,
        "id": id,
        "comment_title": comment_title,
        "content": content,
        "version": v,
        "comment_id": comment_id,
    }