from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from src.dependencies import URLRepoDep
from src.services.read import ReadServise

long_url_router = APIRouter()

@long_url_router.get("/{short_url}", response_class=RedirectResponse)
async def get_long_url(short_url: str, repository: URLRepoDep):
    servise = ReadServise(repository)
    return await servise.get_long_url(short_url)
