#!/bin/sh
# configs
requirement_file=./requirement.txt

#export env file
export $(cat ./.env | xargs )

## build env
#pip install --upgrade pip
#pip install -r $requirement_file
#
## make DB
#ls -la
#./FeatureFlag/manage.py migrate

# run gunicorn

gunicorn --bind $host:$port FeatureFlag.wsgi:application --chdir FeatureFlag/



