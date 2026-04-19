from fastapi import Depends
from typing import Annotated
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db import get_async_session
from src.repositories.db_repo import AsyncDBManager
from src.repositories.url import URLRepository

AsyncSessionDep = Annotated[AsyncSession, Depends(get_async_session)]

def get_async_db_manager(session: AsyncSessionDep)->AsyncDBManager:
    db_manager = AsyncDBManager(session)
    return db_manager

AsyncDBManagerDep = Annotated[AsyncDBManager, Depends(get_async_db_manager)]

def get_url_repo(session: AsyncSessionDep) -> URLRepository:
    db_manager = AsyncDBManager(session)
    repo = URLRepository(db_manager)
    return repo

URLRepoDep = Annotated[URLRepository, Depends(get_url_repo)]