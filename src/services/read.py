from datetime import datetime
from src.models import URL
from src.repositories.url import URLRepository
from src.exceptions.domain import ShortUrlNotFoundError, ShortUrlExpired

class ReadServise:
    def __init__(self, repo: URLRepository):
        self._repo = repo

    async def get_long_url(self, short_url: str) -> str:
        results = await self._repo.get_url(short_url)
        url: URL = results.first()

        if not url:
            raise ShortUrlNotFoundError(short_url)
        
        if url.expires_at < datetime.now():
            raise ShortUrlExpired(short_url)

        return url.long_url
