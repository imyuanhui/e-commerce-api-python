# Generated by Django 5.1.4 on 2024-12-12 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0007_user_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.CharField(max_length=100),
        ),
    ]