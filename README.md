## Kafka to Clickhouse

[![python](https://img.shields.io/static/v1?label=python&message=3.8%20|%203.9%20|%203.10&color=informational)](https://github.com/8ubble8uddy/kafka-to-clickhouse/actions/workflows/main.yml)
[![dockerfile](https://img.shields.io/static/v1?label=dockerfile&message=published&color=2CB3E8)](https://hub.docker.com/r/8ubble8uddy/kafka_to_clickhouse)
[![last updated](https://img.shields.io/static/v1?label=last%20updated&message=february%202023&color=yellow)](https://img.shields.io/static/v1?label=last%20updated&message=february%202022&color=yellow)
[![lint](https://img.shields.io/static/v1?label=lint&message=flake8%20|%20mypy&color=brightgreen)](https://github.com/8ubble8uddy/kafka-to-clickhouse/actions/workflows/main.yml)
[![code style](https://img.shields.io/static/v1?label=code%20style&message=WPS&color=orange)](https://wemake-python-styleguide.readthedocs.io/en/latest/)
[![platform](https://img.shields.io/static/v1?label=platform&message=linux%20|%20macos&color=inactive)](https://github.com/8ubble8uddy/kafka-to-clickhouse/actions/workflows/main.yml)

### **Описание**

_Целью данного проекта является реализация ETL-системы для аналитиков, которая сохраненяет метки данных о просмотрах фильмов. В связи с тем что сервис должен выдерживать запись постоянно поступающей информации от каждого пользователя, в приложении используется платформа для стриминга событий [Kafka](https://kafka.apache.org). Для прослойки кода в виде API, которая под капотом без каких-либо преобразований отправляет событие в Kafka, применяется фреймворк [FastAPI](https://fastapi.tiangolo.com). ETL-процесс для загрузки данных в аналитическое хранилище реализован с помощью библиотеки пакетной и потоковой обработки данных [PySpark](https://spark.apache.org). Хранилище должно обрабатывать очень большие данные и делать это за приемлемое время, где аналитики могли бы проводить свои исследования. Поэтому в рамках проекта было проведено исследование по выбору хранилища, в результате которого наилучшим выбором оказалась аналитическая OLAP-система [Clickhouse](https://clickhouse.com) ._

### **Технологии**

```Python``` ```Kafka``` ```FastAPI``` ```PySpark``` ```Clickhouse``` ```Vertica``` ```Jupyter Notebook``` ```Docker```

### **Как запустить проект:**

Клонировать репозиторий и перейти внутри него в директорию ```/infra```:
```
git clone https://github.com/8ubble8uddy/kafka-to-clickhouse.git
```
```
cd kafka-to-clickhouse/infra/
```

Создать файл .env и добавить настройки для проекта:
```
nano .env
```
```
# Kafka
KAFKA_HOST=kafka
KAFKA_PORT=9092

# Clickhouse
CLICKHOUSE_HOST=clickhouse-node1
CLICKHOUSE_PORT=9000
```

Развернуть и запустить проект в контейнерах:
```
docker-compose up
```

Отправить POST-запрос с текущим фреймом просмотра фильма:
```
http://127.0.0.1/films/<UUID>/video_progress
```
```
{
    "frame": <INTEGER>
}
```

### Автор: Герман Сизов