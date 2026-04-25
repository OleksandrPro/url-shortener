from src.repositories.db_repo import SyncDBManager 
from src.models import Counter
from sqlmodel import select

class CounterRepository:
    def __init__(self, db_manager: SyncDBManager):
        self._db_manager = db_manager

    def get_counter(self) -> Counter | None:
        statement = select(Counter)

        result = self._db_manager.get_record(statement)

        return result.first()
    
    def update(self, new_counter: Counter) -> Counter:
        return self._db_manager.update_record(new_counter)
    