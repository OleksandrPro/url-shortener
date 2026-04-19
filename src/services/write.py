from src.models import ShortUrlCreate, URL
from src.repositories.url import URLRepository
from .short_url_generator import generate_short_url

class WriteService:
    def __init__(self, repo: URLRepository):
        self._repo = repo

    async def create_short_url(self, data: ShortUrlCreate):
        if data.custom_short_url:
            print(data)
            result = await self._repo.get_url(short_url=data.custom_short_url)
            entry = result.first()
            print(f"result: {entry}")
            print("----------------")
            if entry:
                raise Exception("This short url already exists")

            short = data.custom_short_url
        else:
            short = generate_short_url(data.long_url)

        final_data = URL(short_url=short, long_url=data.long_url)
        print(f"final_data: {final_data}")
        
        return await self._repo.add_new_url(final_data)
    
