from sqlmodel import Session, select
from src.repositories.db_repo import SyncDBManager
from src.db import sync_engine
from src.models import Counter

def seed_counter(db_manager: SyncDBManager, init_counter: Counter):
    statement = select(Counter).where(Counter.id==1)

    result = db_manager.get_record(statement)

    entry = result.first()

    if not entry:
        db_manager.add_record(init_counter)

def seed_data(db_manager: SyncDBManager):
    init_counter = Counter(id=1, current_count=0)
    seed_counter(db_manager, init_counter)

if __name__ == "__main__":
    with Session(sync_engine) as session:
        
        db_manager = SyncDBManager(session)
        seed_data(db_manager)