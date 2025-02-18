from fastapi import APIRouter

from app.api.routes import tags, auth

router = APIRouter()

router.include_router(tags.router, tags=["tags"], prefix="/tags")
router.include_router(auth.router, tags=["auth"], prefix="/auth")
