# Generated by Django 4.2.7 on 2023-11-28 13:33

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicationid', models.CharField(max_length=40, null=True)),
                ('description', models.CharField(max_length=40, null=True)),
                ('name', models.CharField(max_length=40, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_domestic', models.BooleanField(null=True)),
            ],
            options={
                'verbose_name_plural': 'پولی واحد',
            },
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=30, unique=True)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_code', models.IntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)])),
                ('location_name', models.CharField(max_length=40, unique=True)),
                ('location_contact', models.CharField(max_length=40)),
                ('location_email', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name_plural': 'موقعیت',
            },
        ),
        migrations.CreateModel(
            name='NawaSanad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nawa_sanad', models.CharField(max_length=15, unique=True)),
                ('nawa_sanad_code', models.IntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('description', models.CharField(blank=True, max_length=15, null=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'نوع سند',
            },
        ),
        migrations.CreateModel(
            name='Language_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('value', models.TextField(null=True)),
                ('page', models.CharField(blank=True, max_length=30, null=True)),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='configuration.languages')),
            ],
            options={
                'verbose_name_plural': 'ترجمه',
                'unique_together': {('language', 'key')},
            },
        ),
        migrations.CreateModel(
            name='Assign_Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('languages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.languages')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Language',
                'unique_together': {('languages', 'user')},
            },
        ),
    ]