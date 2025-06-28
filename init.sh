#! /bin/sh

python manage.py migrate


# create admin
python manage.py createsuperuser

# seed data
python manage.py loaddata grains
python manage.py loaddata categories
python manage.py loaddata colors
