from fastapi import Depends
from typing import Annotated
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import Session
from src.db import get_async_session, get_sync_session
from src.repositories.db_repo import AsyncDBManager, SyncDBManager
from src.repositories.url import URLRepository
from src.repositories.counter import CounterRepository

AsyncSessionDep = Annotated[AsyncSession, Depends(get_async_session)]

def get_async_db_manager(session: AsyncSessionDep)->AsyncDBManager:
    db_manager = AsyncDBManager(session)
    return db_manager

AsyncDBManagerDep = Annotated[AsyncDBManager, Depends(get_async_db_manager)]

SyncSessionDep = Annotated[Session, Depends(get_sync_session)]

def get_sync_db_manager(session: SyncSessionDep)->SyncDBManager:
    db_manager = SyncDBManager(session)
    return db_manager

SyncDBManagerDep = Annotated[SyncDBManager, Depends(get_sync_db_manager)]

def get_url_repo(db_manager: AsyncDBManagerDep) -> URLRepository:
    repo = URLRepository(db_manager)
    return repo

URLRepoDep = Annotated[URLRepository, Depends(get_url_repo)]

def get_counter_repo(db_manager: SyncDBManagerDep) -> CounterRepository:
    repo = CounterRepository(db_manager)
    return repo

CounterRepoDep = Annotated[CounterRepository, Depends(get_counter_repo)]