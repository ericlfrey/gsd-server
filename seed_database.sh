#!/bin/bash

rm db.sqlite3
rm -rf ./gsdapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations gsdapi
python3 manage.py migrate gsdapi
python3 manage.py loaddata client_data
python3 manage.py loaddata project_data
python3 manage.py loaddata task_data
python3 manage.py loaddata material_data

# for Heroku:

heroku run python3 manage.py migrate


heroku run python3 manage.py loaddata client_data --app gsd-api
heroku run python3 manage.py loaddata project_data --app gsd-api
heroku run python3 manage.py loaddata task_data --app gsd-api
heroku run python3 manage.py loaddata material_data --app gsd-api
