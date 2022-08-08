FROM python:3.9

RUN apt update && apt install build-essential -y --no-install-recommends

RUN export $(cat ./.env | xargs )

WORKDIR /code/
EXPOSE $port
COPY . /code/

CMD ["/bin/bash", "run.sh"]

