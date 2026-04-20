from src.models import ShortUrlCreate, URL
from src.repositories.url import URLRepository
from .short_url_generator import generate_short_url
from src.exceptions.domain import UrlAlreadyExistsException

class WriteService:
    def __init__(self, repo: URLRepository):
        self._repo = repo

    async def create_short_url(self, data: ShortUrlCreate):
        if data.custom_short_url:
            result = await self._repo.get_url(short_url=data.custom_short_url)
            entry = result.first()
            if entry:
                raise UrlAlreadyExistsException(f"{data.custom_short_url}")

            short = data.custom_short_url
        else:
            short = generate_short_url(data.long_url)

        final_data = URL(short_url=short, long_url=data.long_url)
        
        return await self._repo.add_new_url(final_data)
    
