FROM python:3.11

WORKDIR /app

COPY backend/ /app

RUN pip install django redis

CMD ["python", "manage.py", "runserver", "0.0.0.0:10000"]
