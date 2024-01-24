# Generated by Django 4.2.7 on 2024-01-23 13:45

import datetime
from django.db import migrations, models
import django.db.models.deletion
import logs.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '__first__'),
        ('haziri', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaceLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=logs.models.image_path)),
                ('is_correct', models.BooleanField(default=False)),
                ('date', models.DateField(default=datetime.datetime(1402, 11, 3, 0, 0))),
                ('year', models.SmallIntegerField(default='1402')),
                ('month', models.SmallIntegerField(default='11')),
                ('day', models.SmallIntegerField(default='03')),
                ('created', models.TimeField(auto_now=True)),
                ('daily_haziri', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='haziri.daily_haziri')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
    ]
