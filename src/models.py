from sqlmodel import SQLModel, Field

class URL(SQLModel, table=True):
    short_url: str = Field(primary_key=True)
    long_url: str
    