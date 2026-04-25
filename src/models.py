from sqlmodel import SQLModel, Field

class URL(SQLModel, table=True):
    short_url: str = Field(primary_key=True)
    long_url: str

class ShortUrlCreate(SQLModel):
    long_url: str
    custom_short_url: str | None = None

class LongUrlGet(SQLModel):
    short_url: str

class Counter(SQLModel, table=True):
    id: int = Field(primary_key=True)
    current_count: int