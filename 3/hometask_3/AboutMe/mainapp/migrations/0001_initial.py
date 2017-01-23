# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-01-23 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(max_length=32, verbose_name='Организиция')),
                ('region', models.CharField(blank=True, max_length=32, verbose_name='Регион')),
                ('site', models.CharField(blank=True, max_length=64, verbose_name='Сайт')),
                ('position', models.CharField(max_length=16, verbose_name='Должность')),
                ('duties', models.TextField(verbose_name='Обязанности')),
                ('period', models.PositiveIntegerField(default=1, verbose_name='Время работы')),
            ],
        ),
    ]
