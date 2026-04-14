FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install django redis

CMD ["python", "manage.py", "runserver", "0.0.0.0:10000"]
