#!/bin/bash

rm db.sqlite3
rm -rf ./gsdapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations gsdapi
python3 manage.py migrate gsdapi
python3 manage.py loaddata project_data
python3 manage.py loaddata task_data
python3 manage.py loaddata material_data
