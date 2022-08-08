FROM python:3.9

RUN apt update && apt install build-essential libpq-dev python-dev -y --no-install-recommends

RUN export $(cat ./.env | xargs )

WORKDIR /code/
EXPOSE $port
COPY . /code/
RUN pip install poetry
RUN poetry install -n --no-root --no-dev

CMD ["/bin/bash", "run.sh"]

