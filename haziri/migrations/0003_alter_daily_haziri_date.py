# Generated by Django 4.2.7 on 2023-12-09 13:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haziri', '0002_rename_user_id_daily_haziri_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_haziri',
            name='date',
            field=models.DateField(default=datetime.datetime(1402, 9, 18, 0, 0)),
        ),
    ]
