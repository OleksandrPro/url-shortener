from fastapi import APIRouter
from src.dependencies import URLRepoDep
from src.services.read import get_long_url as get_long_url_servise

long_url_router = APIRouter(prefix="/long-url")

@long_url_router.get("/{short_url}")
async def get_long_url(short_url: str, repository: URLRepoDep):
    return await get_long_url_servise(short_url, repository)
