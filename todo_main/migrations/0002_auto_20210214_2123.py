# Generated by Django 3.1.6 on 2021-02-14 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_main', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProjectCode',
        ),
        migrations.DeleteModel(
            name='TodoList',
        ),
    ]
