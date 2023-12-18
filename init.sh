#!/bin/bash

pip install --upgrade pip && pip install -r requirements.txt
django-admin startproject blog

if [ -d ./blog ]; then
  cd ./blog
  python manage.py migrate
  python manage.py runserver 127.0.0.1:8000
fi