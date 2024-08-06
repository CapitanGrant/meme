# Meme Collection API

## Функциональность

- GET /memes: Получить список всех мемов (с пагинацией).
- GET /memes/{id}: Получить конкретный мем по его ID.
- POST /memes: Добавить новый мем (с картинкой и текстом).
- PUT /memes/{id}: Обновить существующий мем.
- DELETE /memes/{id}: Удалить мем.

## Требования

- Docker
- Docker Compose

## Запуск проекта

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/your-username/meme_project.git
    cd meme_project
    ```

2. Запустите проект с помощью Docker Compose:
    ```bash
    docker-compose up
