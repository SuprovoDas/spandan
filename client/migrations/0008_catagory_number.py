# Generated by Django 3.0.7 on 2020-09-24 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_auto_20200924_0212'),
    ]

    operations = [
        migrations.AddField(
            model_name='catagory',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
