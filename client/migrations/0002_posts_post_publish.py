# Generated by Django 3.0.7 on 2020-09-19 09:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='post_publish',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
