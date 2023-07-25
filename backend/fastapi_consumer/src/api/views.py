from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException, Response

from api.v1.events import get_film_event
from services.post_event import PostEventService
from models.value import VideoProgress

router = APIRouter()


@router.post(
    '/films/{film_id}/video_progress',
    summary='Отправить текущее время просмотра фильма',
    description='Сохранение отметки времени в секундах, где пользователь остановился при последнем просмотре фильма',
    tags=['films'])
async def send_film_progress(video_progress: VideoProgress, film_event: PostEventService = Depends(get_film_event)):
    """Функция-обработчик для публикации текущего времени просмотра фильма в Kafka.

    Args:
        video_progress: Метка данных о просмотре видео
        film_event: Сервис для публикации события

    Raises:
        HTTPException: Ошибка 400, если сервер Kafka недоступен

    Returns:
        Response: HTTP-ответ с кодом 200
    """
    ok = await film_event.post(video_progress)
    if not ok:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST)
    return Response(status_code=HTTPStatus.CREATED)
