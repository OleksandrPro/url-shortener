from fastapi import APIRouter
from src.dependencies import URLRepoDep
from src.models import ShortUrlCreate, URL
from src.services.write import WriteService

short_url_router = APIRouter(prefix="/short-url")


@short_url_router.post("/", response_model=URL)
async def create_short_url(new_url_data: ShortUrlCreate, repo: URLRepoDep):
    servise = WriteService(repo)
    return await servise.create_short_url(data=new_url_data)