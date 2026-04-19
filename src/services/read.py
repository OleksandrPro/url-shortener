from src.models import URL
from src.repositories.url import URLRepository

async def get_long_url(short_url: str, repo: URLRepository):
    results = await repo.get_url(short_url)
    url: URL = results.first()

    return url.long_url