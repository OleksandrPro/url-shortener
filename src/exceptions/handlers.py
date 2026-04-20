from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from .base import UrlShortenerError
from .domain import UrlAlreadyExistsException, ShortUrlNotFoundError

EXCEPTION_STATUS_MAP = {
    UrlAlreadyExistsException: status.HTTP_400_BAD_REQUEST,

    ShortUrlNotFoundError: status.HTTP_404_NOT_FOUND
}

def register_exception_handlers(app: FastAPI):
    @app.exception_handler(UrlShortenerError)
    async def domain_exception_handler(request: Request, exc: UrlShortenerError):

        status_code = EXCEPTION_STATUS_MAP.get(type(exc), status.HTTP_400_BAD_REQUEST)

        return JSONResponse(
            status_code=status_code,
            content={"detail": str(exc)},
        )