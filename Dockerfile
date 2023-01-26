FROM python:3.11-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

ENV APP_HOST="0.0.0.0"
ENV APP_PORT=3001
ENV EXPORTER_PORT=9877
ENV POLLING_INTERVAL_SECONDS=5

CMD [ "python3", "main.py"]
