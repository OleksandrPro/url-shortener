from fastapi import APIRouter, Depends
from typing import Annotated
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db import get_async_session
from src.repositories.db_repo import AsyncDBManager
from src.repositories.url import URLRepository
from src.services.read import get_long_url as get_long_url_servise

long_url_router = APIRouter(prefix="/long-url")

AsyncSessionDep = Annotated[AsyncSession, get_async_session]

def get_url_repo(session: AsyncSession = Depends(get_async_session)):
    db_manager = AsyncDBManager(session)
    repo = URLRepository(db_manager)
    return repo

URLRepoDep = Annotated[URLRepository, Depends(get_url_repo)]

@long_url_router.get("/{short_url}")
async def get_long_url(short_url: str, repository: URLRepoDep):
    return await get_long_url_servise(short_url, repository)
