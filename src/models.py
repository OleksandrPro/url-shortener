from sqlmodel import SQLModel, Field
from datetime import datetime, timedelta
from src.constants import Config

class URL(SQLModel, table=True):
    short_url: str = Field(primary_key=True)
    long_url: str
    created_at: datetime = Field(
        default_factory=lambda: datetime.now()
    )
    expires_at: datetime = Field(
        default_factory=lambda: datetime.now() + timedelta(minutes=Config.LINK_EXPIRATION_MINUTES)
    )

class ShortUrlCreate(SQLModel):
    long_url: str
    custom_short_url: str | None = None

class LongUrlGet(SQLModel):
    short_url: str

class Counter(SQLModel, table=True):
    id: int = Field(primary_key=True)
    current_count: int