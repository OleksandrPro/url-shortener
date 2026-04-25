from src.models import Counter
from src.repositories.counter import CounterRepository

class CounterService:
    def __init__(self, repo: CounterRepository):
        self._repo = repo
    
    def get_current_count(self) -> int:
        counter = self._repo.get_counter()
        if not counter:
            raise Exception("Counter not found")
        
        return counter.current_count
    
    def get_next_count(self) -> int:
        return self.get_current_count() + 1

    def increment_counter(self) -> Counter:
        counter = self._repo.get_counter()
        if not counter:
            raise Exception("Counter not found")
        
        counter.current_count += 1

        return self._repo.update(counter)