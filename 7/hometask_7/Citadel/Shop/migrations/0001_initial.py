# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-02-07 10:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='Навание')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.Category')),
            ],
        ),
    ]
