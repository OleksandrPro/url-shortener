from src.models import ShortUrlCreate, URL
from src.repositories.url import URLRepository
from src.services.counter import CounterService
from .short_url_generator import generate_short_url
from src.exceptions.domain import UrlAlreadyExistsException
from src.utils import make_url
from src.constants import Config

class WriteService:
    def __init__(self, url_repo: URLRepository, counter_servise = CounterService) -> str:
        self._url_repo = url_repo
        self._counter_servise = counter_servise

    async def create_short_url(self, data: ShortUrlCreate):
        if not data.custom_short_url:
            short = generate_short_url(data.long_url, self._counter_servise)
        else:
            result = await self._url_repo.get_url(short_url=data.custom_short_url)
            entry = result.first()
            if entry:
                raise UrlAlreadyExistsException(f"{data.custom_short_url}")

            short = data.custom_short_url

        final_data = URL(short_url=short, long_url=data.long_url)
        
        record = await self._url_repo.add_new_url(final_data)

        full_link = make_url(Config.HOST, record.short_url)
    
        return full_link 
    
