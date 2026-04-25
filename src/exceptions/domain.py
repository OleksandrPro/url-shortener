from .base import UrlShortenerError

class UrlAlreadyExistsException(UrlShortenerError):
    def __init__(self, url: str):
        super().__init__(f"Short url '{url}' already exists")

class ShortUrlNotFoundError(UrlShortenerError):
    def __init__(self, url: str):
        super().__init__(f"Short url '{url}' doesn't exist")

class ShortUrlExpired(UrlShortenerError):
    def __init__(self, url: str):
        super().__init__(f"Short url '{url}' has expired")