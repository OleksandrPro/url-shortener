from .base import UrlShortenerError

class UrlAlreadyExistsException(UrlShortenerError):
    def __init__(self, url: str):
        super().__init__(f"Short url '{url}' already exists")

class ShortUrlNotFoundError(UrlShortenerError):
    def __init__(self, url: str):
        super().__init__(f"Short url '{url}' doesn't exist")

class ShortUrlGenerationError(UrlShortenerError):
    def __init__(self, url: str, details: str = "internal error"):
        super().__init__(f"Failed to generate short URL for '{url}'. Details: {details}")

class ShortUrlExpired(UrlShortenerError):
    def __init__(self, url: str):
        super().__init__(f"Short url '{url}' has expired")