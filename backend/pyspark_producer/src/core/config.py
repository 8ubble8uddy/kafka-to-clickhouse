from functools import lru_cache

from pydantic import BaseModel, BaseSettings, Field


class KafkaConfig(BaseModel):
    """Класс с настройками подключения к Kafka."""

    host: str = 'localhost'
    port: int = 29092


class ClickhouseConfig(BaseModel):
    """Класс с настройками подключения к Clickhouse."""

    host: str = 'localhost'
    port: int = 9000
    user: str = 'default'
    password: str = ''
    dbname = 'default'
    driver: str = 'com.github.housepower.jdbc.ClickHouseDriver'


class PysparkConfig(BaseModel):
    """Класс с настройками подключения к Pyspark."""

    name = 'kafka_to_clickhouse'


class MainSettings(BaseSettings):
    """Класс с основными настройками проекта."""

    pyspark: PysparkConfig = Field(default_factory=PysparkConfig)
    kafka: KafkaConfig = Field(default_factory=KafkaConfig)
    clickhouse: ClickhouseConfig = Field(default_factory=ClickhouseConfig)


@lru_cache()
def get_settings():
    """Функция для создания объекта настроек в едином экземпляре (синглтона).

    Returns:
        MainSettings: Объект с настройками
    """
    return MainSettings(_env_file='.env', _env_nested_delimiter='_')


CONFIG = get_settings()
