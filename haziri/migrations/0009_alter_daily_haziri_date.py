# Generated by Django 4.2.7 on 2023-12-28 07:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haziri', '0008_howmanytimehaziri_validtimehaziri_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_haziri',
            name='date',
            field=models.DateField(default=datetime.datetime(1402, 10, 6, 0, 0)),
        ),
    ]