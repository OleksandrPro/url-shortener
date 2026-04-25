from src.services.counter import CounterService
from src.utils.encoding.base62 import encode

def generate_short_url(long_url: str, c_servise: CounterService):
    new_count = c_servise.get_next_count()
    """
    
    val = 3900
    short_url = encode(val)
    init_long_url = decode(short_url)

    print(f"----short_url: {short_url}----")
    print(f"----init_long_url: {init_long_url}----")
    """
    try:
        short_url = encode(new_count)
        c_servise.increment_counter()
    except:
        #TODO: fill the except part
        pass
    
    return short_url
