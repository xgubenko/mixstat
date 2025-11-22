# 1. Лёгкий Python образ
FROM python:3.14-slim

# 2. Рабочая директория
WORKDIR /app

# 3. Установка зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Копируем код проекта
COPY . .

# 5. Точка входа
CMD ["python", "main.py"]
