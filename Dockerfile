# Використовуйте офіційний образ Python з встановленою версією, яку ви використовуєте
FROM python:3.12

# Встановлюємо залежності
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копіюємо весь вміст поточної директорії у контейнер
COPY . /app

# Запускаємо ваш консольний додаток
CMD ["python", "-m", "assistant.main"]

