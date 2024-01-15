#!/bin/bash

pip install --upgrade pip && pip install -r requirements.txt
#django-admin startproject mt5_app

cd ./mt5_app

python manage.py migrate
python manage.py runserver 0.0.0.0:8000
