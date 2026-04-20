from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.sql.base import Executable

class AsyncDBManager:
    def __init__(self, session: AsyncSession):
        self._session = session
    
    async def get_record(self, statement: Executable):
        return await self._session.exec(statement)

    async def add_record(self, new_record: SQLModel):        
        self._session.add(new_record)

        await self._session.commit()

        return new_record
