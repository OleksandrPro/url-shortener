from fastapi import FastAPI
from src.routers.short_url import short_url_router
from src.routers.long_url import long_url_router
from src.exceptions.handlers import register_exception_handlers

app = FastAPI()


app.include_router(short_url_router)
app.include_router(long_url_router)

register_exception_handlers(app)