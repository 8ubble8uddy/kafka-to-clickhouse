from functools import lru_cache

from aiokafka import AIOKafkaProducer
from fastapi import Depends, Path

from api.v1.auth import Auth
from services.post_event import PostEventService
from core.enums import KafkaTopics
from db.kafka import get_kafka
from models.key import UserFilmID


@lru_cache()
def get_film_event(
    auth: Auth = Depends(),
    film_id: str = Path(title='Фильм ID'),
    kafka: AIOKafkaProducer = Depends(get_kafka),
):
    """Функция провайдер для PostEventService, чтобы отправить относящиеся к фильму событие.

    Args:
        auth: Аутентификация пользователя
        film_id: ID фильма
        kafka: Подключение к Kafka

    Returns:
        PostEventService: Сервис для публикации места в фильме, где остановился пользователь
    """
    return PostEventService(
        kafka=kafka,
        topic=KafkaTopics.video_progress.name,
        key=UserFilmID(user_id=auth.user_id, film_id=film_id),
    )
