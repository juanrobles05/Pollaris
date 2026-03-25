from fastapi import FastAPI

from app.api.api_v1 import api_router as api_v1

from .core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

app.include_router(api_v1, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "Pollaris is running!"}
