# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-01-23 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(max_length=32, verbose_name='Место обучения')),
                ('region', models.CharField(blank=True, max_length=32, verbose_name='Регион')),
                ('site', models.CharField(blank=True, max_length=64, verbose_name='Сайт')),
                ('start_date', models.DateField(default='2007-09-01', verbose_name='Начало обучения')),
                ('end_date', models.DateField(default='2007-09-01', verbose_name='Конец обучения')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Обо мне')),
                ('hobby', models.TextField(verbose_name='Хобби')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(max_length=32, verbose_name='Организиция')),
                ('region', models.CharField(blank=True, max_length=32, verbose_name='Регион')),
                ('position', models.CharField(max_length=16, verbose_name='Должность')),
                ('duties', models.TextField(verbose_name='Обязанности')),
                ('start_date', models.DateField(default='2007-09-01', verbose_name='С')),
                ('end_date', models.DateField(default='2007-09-01', verbose_name='До')),
            ],
        ),
    ]
