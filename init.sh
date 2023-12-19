#!/bin/bash

pip install --upgrade pip && pip install -r requirements.txt
#django-admin startproject mt5_app


if [ -d ./mt5_app ]; then
  cd ./mt5_app
  #python3 manage.py startapp blog
  python manage.py migrate
  python manage.py runserver 0.0.0.0:8000
fi