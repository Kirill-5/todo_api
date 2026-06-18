# Todo API

Сервис для управления списком задач (To-Do) с JWT-аутентификацией и хранением данных в PostgreSQL.

## Быстрый старт

```bash
# Клонировать репозиторий
git clone https://github.com/Kirill-5/todo_api.git
cd todo_api
```

# Запустить через Docker Compose
docker-compose up --build

Тестовые пользователи
Для тестирования создайте своего пользователя через /auth/register.
Пример:

``
{
  "username": "testuser",
  "password": "testpass"
}
