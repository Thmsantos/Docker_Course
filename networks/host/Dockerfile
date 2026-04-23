FROM python:3

WORKDIR /app

COPY . .

RUN pip install flask requests pymongo

EXPOSE 6000

CMD ["python", "app.py"]