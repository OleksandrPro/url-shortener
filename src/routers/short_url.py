from fastapi import APIRouter
from src.dependencies import URLRepoDep, CounterRepoDep
from src.models import ShortUrlCreate, URL
from src.services.write import WriteService
from src.services.counter import CounterService

short_url_router = APIRouter(prefix="/short-url")


@short_url_router.post("/")
async def create_short_url(new_url_data: ShortUrlCreate, url_repo: URLRepoDep, counter_repo: CounterRepoDep):
    counter_servise = CounterService(counter_repo)
    write_servise = WriteService(url_repo, counter_servise)
    return await write_servise.create_short_url(data=new_url_data)