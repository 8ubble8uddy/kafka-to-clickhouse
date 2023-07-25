from aiokafka import AIOKafkaProducer
from pydantic import BaseModel

from core.enums import KafkaTopics


class EventService(BaseModel):
    """Базовый класс сервиса для мониторига пользовательского контента."""

    kafka: AIOKafkaProducer
    topic: KafkaTopics

    class Config:
        """Настройки валидиции."""

        use_enum_values = True
        arbitrary_types_allowed = True
