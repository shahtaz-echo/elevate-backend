from fastapi import APIRouter
from app.api.routes import health, auth, user

router = APIRouter()

router.include_router(health.router, tags=["health"], prefix="/health")
router.include_router(auth.router, tags=["auth"], prefix="/auth")
router.include_router(user.router, tags=["user"], prefix="/user")
