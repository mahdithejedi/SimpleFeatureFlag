FROM python:3.9

RUN apt update && apt install build-essential -y --no-install-recommends

WORKDIR /code/
COPY . /code/
EXPOSE $port

CMD ["make", "production"]
