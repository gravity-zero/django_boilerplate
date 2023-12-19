#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.db import connections
from dotenv import dotenv_values


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mt5_app.settings')

    # Vérifier la connexion à MySQL
    try:
        connection = connections['default']
        cursor = connection.cursor()
        result = cursor.execute("SELECT 1")
        print("Connexion à MySQL réussie ! SELECT 1 =", result)
    except Exception as e:
        print(f"Erreur de connexion à MySQL : {e}")

    # config = dotenv_values(".env.dev")
    # print("URL du projet .env.dev:", config['ROOT_URL'])

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
