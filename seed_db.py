from typing import List
from sqlmodel import SQLModel, Session
from src.repositories.db_repo import SyncDBManager
from src.db import sync_engine
from src.models import Counter

DATA = [
    Counter(id=1, current_count=0)
]

def seed_data(db_manager: SyncDBManager, init_data: List[SQLModel]):
    for data in init_data:
            db_manager.add_record(new_record=data)

if __name__ == "__main__":
    with Session(sync_engine) as session:
        
        db_manager = SyncDBManager(session)
        seed_data(db_manager, DATA)