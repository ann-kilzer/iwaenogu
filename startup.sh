#!/bin/bash

python3 manage.py migrate

# create admin
python3 manage.py createsuperuser

# seed data
python3 manage.py loaddata grains
python3 manage.py loaddata categories
python3 manage.py loaddata colors