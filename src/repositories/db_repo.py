from sqlmodel import SQLModel, Session
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

class SyncDBManager:
    def __init__(self, session: Session):
        self._session = session
    
    def get_record(self, statement: Executable):
        return self._session.exec(statement)

    def add_record(self, new_record: SQLModel):        
        self._session.add(new_record)

        self._session.commit()

        return new_record
    
    def update_record(self, new_record: SQLModel):        
        self._session.add(new_record)
        self._session.commit()
        self._session.refresh(new_record)

        return new_record