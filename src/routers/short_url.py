from fastapi import APIRouter

short_url_router = APIRouter(prefix="/short-url")

@short_url_router.post("/")
async def create_short_url():
    pass