FROM python:3.9


WORKDIR /app

COPY producer.py /app/producer.py
COPY consumer.py /app/consumer.py

# Встановлення залежностей, якщо вони є
RUN pip install pika
RUN pip install mongoengine

# Команда, яка запускає producer.py та consumer.py при запуску контейнера
CMD ["bash", "-c", "python producer.py & python consumer.py"]