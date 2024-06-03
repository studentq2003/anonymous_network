from fastapi import APIRouter

from .posts.posts import router as post_router

router = APIRouter()
router.include_router(router=post_router, prefix="/posts")
