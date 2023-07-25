from models.base import EventValue


class VideoProgress(EventValue):
    """Модель значения события для записи текущего времени воспроизведения видео."""

    frame: int

    def __str__(self) -> str:
        """Строковое представление сформированного значения события.

        Returns:
            str: Значение события
        """
        return self.json()
