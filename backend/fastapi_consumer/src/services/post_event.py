import logging

from aiokafka.errors import KafkaError

from services.base import EventService
from models.base import EventKey, EventValue


class PostEventService(EventService):
    """Сервис для отправки события в брокер сообщений Kafka."""

    key: EventKey

    async def post(self, value: EventValue) -> bool:
        """Основной метод публикации события в поток.

        Args:
            value: Значение события

        Returns:
            bool: Отправлено сообщение или нет
        """
        try:
            result = await self.kafka.send_and_wait(self.topic, value, self.key)
        except KafkaError as exc:
            logging.error(exc)
            return False
        else:
            logging.info(result)
            return True
