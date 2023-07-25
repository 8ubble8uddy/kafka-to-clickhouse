from uuid import UUID

from models.base import EventKey


class UserFilmID(EventKey):
    """Модель ключа события для партиционирования по пользователям и фильмам."""

    film_id: UUID
    user_id: UUID

    def __str__(self) -> str:
        """Строковое представление сформированного ключа события.

        Returns:
            str: Ключ события
        """
        return f'{self.film_id}::{self.user_id}'
