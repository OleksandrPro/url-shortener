from src.services.counter import CounterService
from src.utils.encoding.base62 import encode

def generate_short_url(c_servise: CounterService):
    new_count = c_servise.get_next_count()

    try:
        short_url = encode(new_count)
        c_servise.increment_counter()
    except:
        #TODO: fill the except part
        pass
    
    return short_url
