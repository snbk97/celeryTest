FROM ubuntu:20.04

WORKDIR /app

COPY . ./app/

RUN cd app && apt update;\
    apt install -y redis-server systemd python3-pip;\
    which redis &&\
    systemctl start redis;\
    pip3 install poetry

RUN cd app && poetry config virtualenvs.create false &&\
    poetry install --no-dev --no-interaction --no-ansi &&\
    celery -A tasks worker --loglevel=info --uid=0

# RUN celery -A tasks worker --loglevel=info

RUN python3 app.py

EXPOSE 5000