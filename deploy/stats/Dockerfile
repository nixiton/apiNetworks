# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
CMD pip install -r require.txt && python manage.py runserver 0.0.0.0:8000 && python manage.py makemigrations && python manage.py migrate
# coverage run manage.py test
# coverage report 
