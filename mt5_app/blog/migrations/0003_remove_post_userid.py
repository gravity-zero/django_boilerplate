# Generated by Django 3.2 on 2023-12-19 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='userID',
        ),
    ]