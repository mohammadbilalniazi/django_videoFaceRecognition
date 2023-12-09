# Generated by Django 4.2.7 on 2023-12-09 13:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0002_alter_log_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='date',
            field=models.DateField(default=datetime.datetime(1402, 9, 18, 0, 0)),
        ),
        migrations.AlterField(
            model_name='log',
            name='created',
            field=models.TimeField(auto_now=True),
        ),
    ]