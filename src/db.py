from sqlmodel import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from src.constants import DB

sync_engine = create_engine(DB.SYNC_URL, echo=True)
async_engine = create_async_engine(DB.ASYNC_URL)

async_session_factory = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False
)

async def get_async_session():
    async with async_session_factory() as session:
        yield session