# Todo API

Сервис для управления списком задач (To-Do) с JWT-аутентификацией и хранением данных в PostgreSQL.

## Что нового в этом проекте (по сравнению с https://github.com/Kirill-5/booking_project)
- Код разбит на логические слои (api, core, models, schemas, db) вместо одного файла.
- В тестах используются фикстуры pytest для очистки БД.




## Быстрый старт

```bash
# Клонировать репозиторий
git clone https://github.com/Kirill-5/todo_api.git
cd todo_api
```

# Запустить через Docker Compose
```
docker-compose up --build
```

Тестовые пользователи
Для тестирования создайте своего пользователя через /auth/register.
Пример:

```bash
{
  "username": "testuser",
  "password": "testpass"
}
```


# API Эндпоинты
Все эндпоинты (кроме /auth/register и /auth/login) требуют JWT токен в заголовке:
```
Authorization: Bearer <ваш_токен>
```

| Метод | Эндпоинт | Описание |
|-------|----------|----------|
| POST | 	/auth/register  |	Регистрация нового пользователя
| POST | 	/auth/login  |	Получение JWT токена
| GET | 	/todos/  |	Список всех задач пользователя
| POST | 	/todos/  |	Создать новую задачу
| PATCH | 	/todos/{id}  |	Обновить задачу (например, отметить выполненной)
| DELETE | 	/todos/{id}  |	Удалить задачу


# Запуск тестов
## Убедиться, что БД запущена (если не через Docker Compose)
```
docker start todo_postgres
```

## Запустить все тесты
```
poetry run pytest tests/ -v
```

# Структура проекта

```
todo_api/
├── app/                                # Основная директория приложения
│   ├── api/                            # Слой маршрутов и зависимостей
│   │   ├── routes/                     # Эндпоинты
│   │   │   ├── auth.py                 # Регистрация и логин (JWT)
│   │   │   └── todos.py                # CRUD для задач
│   │   └── dependencies.py             # Общие зависимости (например, get_db)
│   ├── core/                           # Настройки и безопасность
│   │   ├── config.py                   # Настройки из .env
│   │   └── security.py                 # JWT (AuthX) — конфиг и функции
│   ├── db/                             # База данных
│   │   └── database.py                 # Подключение к PostgreSQL, сессии, Base
│   ├── models/                         # Модели SQLAlchemy
│   │   ├── user.py                     # Модель пользователя
│   │   └── todo.py                     # Модель задачи
│   ├── schemas/                        # Pydantic схемы для валидации
│   │   ├── token.py                    # Схема для токена
│   │   ├── user.py                     # Схемы для регистрации/ответа
│   │   └── todo.py                     # Схемы для задач (Create, Update, Response)
│   └── main.py                         # Точка входа FastAPI
├── tests/                              # Тесты
│   ├── test_auth.py                    # Тесты регистрации и логина
│   ├── test_todos.py                   # Тесты CRUD задач
│   └── conftest.py                     # Фикстуры для тестов (очистка БД, клиент)
├── Dockerfile                          # Инструкция для сборки образа
├── docker-compose.yml                  # Запуск приложения и PostgreSQL
├── pyproject.toml                      # Зависимости (poetry)
├── poetry.lock                         # Фиксация версий зависимостей
└── README.md                           # Документация
```



## Технологии
- Python 3.12
- FastAPI
- PostgreSQL + SQLAlchemy
- JWT (AuthX)
- Docker / Docker Compose
- Pytest
