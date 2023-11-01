FROM python:3.10-slim

WORKDIR /api_service

RUN apt-get update && apt-get --yes upgrade

COPY requirements.txt requirements.txt
RUN  pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

COPY . .

RUN chmod +x /api_service/docker-entrypoint.sh
RUN chmod +x /api_service/wait-for-it.sh

ENTRYPOINT sh /api_service/docker-entrypoint.sh

EXPOSE 8000