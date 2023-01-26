FROM python:3.11-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

ENV APP_HOST
ENV APP_PORT
ENV EXPORTER_PORT
ENV POLLING_INTERVAL_SECONDS

CMD [ "python3", "main.py"]