from functools import lru_cache
from logging import config as logging_config

from pydantic import BaseModel, BaseSettings, Field

from core.logger import LOGGING

logging_config.dictConfig(LOGGING)


class KafkaConfig(BaseModel):
    """Класс с настройками подключения к Kafka."""

    host: str = 'localhost'
    port: int = 29092


class FastApiConfig(BaseModel):
    """Класс с настройками подключения к FastAPI."""

    host: str = '0.0.0.0'
    port: int = 8000
    debug: bool = False
    docs: str = 'openapi'
    title: str = 'Post-only API для мониторинга пользовательского контента'
    secret_key: str = 'secret_key'


class MainSettings(BaseSettings):
    """Класс с основными настройками проекта."""

    fastapi: FastApiConfig = Field(default_factory=FastApiConfig)
    kafka: KafkaConfig = Field(default_factory=KafkaConfig)


@lru_cache()
def get_settings():
    """Функция для создания объекта настроек в едином экземпляре (синглтона).

    Returns:
        MainSettings: Объект с настройками
    """
    return MainSettings(_env_file='.env', _env_nested_delimiter='_')


CONFIG = get_settings()
