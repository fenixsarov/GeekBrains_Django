from django.db import models

class Index(models.Model):
    description = models.TextField(verbose_name='Обо мне')
    hobby = models.TextField(verbose_name='Хобби')

class Work(models.Model):
    organization = models.CharField(verbose_name='Организиция', max_length=32)
    region = models.CharField(verbose_name='Регион', max_length=32, blank=True)
    position = models.CharField(verbose_name='Должность', max_length=16)
    duties = models.TextField(verbose_name='Обязанности')
    start_date = models.DateField(verbose_name='С', default='2007-09-01')
    end_date = models.DateField(verbose_name='До', default='2007-09-01')


class Education(models.Model):
    organization = models.CharField(verbose_name='Место обучения', max_length=32)
    region = models.CharField(verbose_name='Регион', max_length=32, blank=True)
    site = models.CharField(verbose_name='Сайт', max_length=64, blank=True)
    start_date = models.DateField(verbose_name='Начало обучения', default='2007-09-01')
    end_date = models.DateField(verbose_name='Конец обучения', default='2007-09-01')
    description = models.TextField(verbose_name='Описание')
