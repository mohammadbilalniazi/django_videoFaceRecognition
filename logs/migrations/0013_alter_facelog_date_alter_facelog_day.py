# Generated by Django 4.2.7 on 2024-01-13 11:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0012_alter_facelog_date_alter_facelog_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facelog',
            name='date',
            field=models.DateField(default=datetime.datetime(1402, 10, 23, 0, 0)),
        ),
        migrations.AlterField(
            model_name='facelog',
            name='day',
            field=models.SmallIntegerField(default='23'),
        ),
    ]
