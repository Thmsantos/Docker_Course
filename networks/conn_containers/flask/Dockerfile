FROM python:3

RUN apt-get update && apt-get install -y python3-pip python3-dev && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /app

RUN pip install Flask requests flask_mysqldb

COPY . .

EXPOSE 5000

CMD ["python", "./app.py"]