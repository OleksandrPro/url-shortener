from src.repositories.db_repo import AsyncDBManager 
from src.models import URL
from sqlmodel import select

class URLRepository:
    def __init__(self, db_manager: AsyncDBManager):
        self._db_manager = db_manager

    async def add_new_url(self, new_url: URL):
        return await self._db_manager.add_record(new_url)

    async def get_url(self, short_url: str) -> URL | None:
        statement = select(URL).where(URL.short_url == short_url)

        return await self._db_manager.get_record(statement)