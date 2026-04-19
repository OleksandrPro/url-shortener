from fastapi import APIRouter

long_url_router = APIRouter(prefix="/long-url")

@long_url_router.get("/{short_url}")
async def get_long_url(short_url: str):
    pass
