import logging

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.views import router
from core.config import CONFIG
from core.logger import LOGGING
from db import _connections as connections

app = FastAPI(
    title=CONFIG.fastapi.title,
    description='Сервис для хранения аналитической информации и UGC',
    version='1.0.0',
    docs_url=f'/{CONFIG.fastapi.docs}',
    openapi_url=f'/{CONFIG.fastapi.docs}.json',
    default_response_class=ORJSONResponse,
)


@app.on_event('startup')
async def startup():
    """Подключаемся к хранилищу событий Kafka при старте сервера."""
    await connections.start_kafka()


@app.on_event('shutdown')
async def shutdown():
    """Отключаемся от хранилища событий Kafka при выключении сервера."""
    await connections.stop_kafka()


app.include_router(router, prefix='/api/v1')

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=CONFIG.fastapi.host,
        port=CONFIG.fastapi.port,
        log_config=LOGGING,
        log_level=logging.DEBUG,
    )
