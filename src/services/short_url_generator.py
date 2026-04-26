from src.services.counter import CounterService
from src.utils.encoding.base62 import encode

def generate_short_url(c_servise: CounterService):
    new_count = c_servise.get_next_count()

    short_url = encode(new_count)
    c_servise.increment_counter()
    
    return short_url
