# FastAPI URL shortener

API-сервис для сокращения ссылок. Реализован на **FastAPI** с использованием **SQLite** и **SQLAlchemy**, обёрнут в **Docker**.  

## ⚙️ Как запустить проект

> Требования: установлен [Docker](https://www.docker.com/) и [Docker Compose](https://docs.docker.com/compose/)

```bash
git clone https://github.com/den13boec/fastapi_url_shortener.git
cd fastapi_url_shortener
docker-compose up --build
```

## Эндпойнты

| Метод | URL                    | Описание                                                                  |
|-------|------------------------|---------------------------------------------------------------------------|
| POST  | `/api/v1/shorten`      | Принимает URL, возвращает короткую ссылку с уникальным 6-символьным кодом |
| GET   | `/s/{code}`            | Выполняет редирект на оригинальный URL и увеличивает счётчик переходов    |
| GET   | `/api/v1/stats/{code}` | Возвращает оригинальный URL, количество переходов и дату создания         |

>Протестировать эндпойнты можно через [SwaggerUI](http://127.0.0.1:8000/docs) или [Redoc](http://127.0.0.1:8000/redoc)
