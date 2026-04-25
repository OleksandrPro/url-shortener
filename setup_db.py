from sqlmodel import SQLModel
from src.models import URL, Counter
from src.db import sync_engine

SQLModel.metadata.create_all(sync_engine)