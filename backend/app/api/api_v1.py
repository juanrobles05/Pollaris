from fastapi import APIRouter

from app.routers import user

api_router = APIRouter()

api_router.include_router(user.router)
