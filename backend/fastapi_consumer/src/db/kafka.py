from typing import Optional

from aiokafka import AIOKafkaProducer

connection: Optional[AIOKafkaProducer] = None


async def get_kafka():
    """Функция для объявления соединения с Kafka, которая понадобится при внедрении зависимостей.

    Returns:
        AIOKafkaProducer: Соединение с Kafka
    """
    return connection
