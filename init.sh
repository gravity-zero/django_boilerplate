#!/bin/bash

pip install --upgrade pip && pip install -r requirements.txt
django-admin startproject blog
cd ./blog

python manage.py runserver 0.0.0.0:8000