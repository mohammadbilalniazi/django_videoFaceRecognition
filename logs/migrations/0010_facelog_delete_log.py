# Generated by Django 4.2.7 on 2023-12-31 06:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('haziri', '0011_alter_daily_haziri_date'),
        ('logs', '0009_alter_log_date_alter_log_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaceLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='logs')),
                ('is_correct', models.BooleanField(default=False)),
                ('date', models.DateField(default=datetime.datetime(1402, 10, 9, 0, 0))),
                ('year', models.SmallIntegerField(default='1402')),
                ('month', models.SmallIntegerField(default='10')),
                ('day', models.SmallIntegerField(default='09')),
                ('created', models.TimeField(auto_now=True)),
                ('daily_haziri', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='haziri.daily_haziri')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
        migrations.DeleteModel(
            name='Log',
        ),
    ]