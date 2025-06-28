#! /bin/sh

python manage.py migrate --noinput

# color picker plugin
python manage.py collectstatic --noinput

# create admin
#python3 manage.py createsuperuser --username

# seed data
python3 manage.py loaddata grains
python3 manage.py loaddata categories
python3 manage.py loaddata colors

