# Generated by Django 5.1.4 on 2024-12-12 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0002_user_is_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
    ]