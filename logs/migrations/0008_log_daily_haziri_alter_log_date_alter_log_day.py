# Generated by Django 4.2.7 on 2023-12-28 07:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('haziri', '0009_alter_daily_haziri_date'),
        ('logs', '0007_log_day_log_month_log_year_alter_log_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='daily_haziri',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='haziri.daily_haziri'),
        ),
        migrations.AlterField(
            model_name='log',
            name='date',
            field=models.DateField(default=datetime.datetime(1402, 10, 6, 0, 0)),
        ),
        migrations.AlterField(
            model_name='log',
            name='day',
            field=models.SmallIntegerField(default='06'),
        ),
    ]