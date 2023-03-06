from fastapi import APIRouter

router = APIRouter(
    prefex="/blog",
    tags=["blog"],
)
