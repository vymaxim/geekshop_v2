# Generated by Django 3.2.7 on 2021-09-23 07:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210923_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 25, 7, 54, 15, 333580, tzinfo=utc)),
        ),
    ]
