FROM python:3.8-alpine

RUN mkdir -p /app
ADD . /app
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]