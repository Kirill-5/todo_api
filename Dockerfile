FROM python:3.12-slim

WORKDIR /app

# Копируем и устанавливаем зависимости через pip
COPY pyproject.toml poetry.lock ./
RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy psycopg2-binary python-jose[cryptography] passlib[bcrypt] python-multipart pytest authx httpx

# Копируем код
COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]