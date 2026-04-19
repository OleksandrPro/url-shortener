from fastapi import APIRouter, Depends
from typing import Annotated
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db import get_async_session
from src.repositories.db_repo import AsyncDBManager
from src.repositories.url import URLRepository
from src.models import ShortUrlCreate
from src.services.write import WriteService

short_url_router = APIRouter(prefix="/short-url")

AsyncSessionDep = Annotated[AsyncSession, get_async_session]

def get_url_repo(session: AsyncSession = Depends(get_async_session)):
    db_manager = AsyncDBManager(session)
    repo = URLRepository(db_manager)
    return repo

URLRepoDep = Annotated[URLRepository, Depends(get_url_repo)]


@short_url_router.post("/")
async def create_short_url(new_url_data: ShortUrlCreate, session = Depends(get_async_session)):
    db_manager = AsyncDBManager(session)
    repo = URLRepository(db_manager)
    servise = WriteService(repo)
    return await servise.create_short_url(data=new_url_data)