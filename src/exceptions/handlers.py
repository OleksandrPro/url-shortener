from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse, HTMLResponse

from .base import UrlShortenerError
from .domain import UrlAlreadyExistsException, ShortUrlNotFoundError, ShortUrlExpired

EXCEPTION_STATUS_MAP = {
    UrlAlreadyExistsException: status.HTTP_400_BAD_REQUEST,

    ShortUrlNotFoundError: status.HTTP_404_NOT_FOUND
}

NOT_FOUND = """
<html>
    <body>
        <h1>Not found</h1>
    </body>
</html>
"""

URL_EXPIRED = """
<html>
    <body>
        <h1>Url has expired!</h1>
    </body>
</html>
"""

SERVER_ERROR = """
<html>
    <body>
        <h1>Internal server error!</h1>
    </body>
</html>
"""

def register_exception_handlers(app: FastAPI):
    @app.exception_handler(UrlShortenerError)
    async def domain_exception_handler(request: Request, exc: UrlShortenerError):

        status_code = EXCEPTION_STATUS_MAP.get(type(exc), status.HTTP_400_BAD_REQUEST)

        match exc:
            case UrlAlreadyExistsException():
                response = JSONResponse(
                    status_code=status_code,
                    content={"detail": str(exc)},
                )
            case ShortUrlNotFoundError():
                response = HTMLResponse(
                    status_code=status_code,
                    content=NOT_FOUND
                )
            case ShortUrlExpired():
                response = HTMLResponse(
                    status_code=status_code,
                    content=URL_EXPIRED
                )

        return response
    
    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception):

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=SERVER_ERROR
        )