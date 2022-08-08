#!/bin/sh
# configs
requirement_file=./requirement.txt

#export env file
export $(cat ./.env | xargs )


# make DB

poetry run ./FeatureFlag/manage.py migrate

# run gunicorn

poetry run gunicorn --bind $host:$port FeatureFlag.wsgi:application --chdir FeatureFlag/



