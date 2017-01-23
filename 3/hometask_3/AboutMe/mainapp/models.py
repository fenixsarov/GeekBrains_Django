from django.db import models


class Work(models.Model):
    organization = models.CharField(verbose_name='Организиция', max_length=32)
    region = models.CharField(verbose_name='Регион', max_length=32, blank=True)
    site = models.CharField(verbose_name='Сайт', max_length=64, blank=True)
    position = models.CharField(verbose_name='Должность', max_length=16)
    duties = models.TextField(verbose_name='Обязанности')
    period = models.PositiveIntegerField(verbose_name='Время работы', default=1)


# Create your models here.

class Education(models.Model):
    organization = models.CharField(verbose_name='Место обучения', max_length=32)
    region = models.CharField(verbose_name='Регион', max_length=32, blank=True)
    site = models.CharField(verbose_name='Сайт', max_length=64, blank=True)
    start_date = models.DateField(verbose_name='Период обучения')
    end_date = models.DateField(verbose_name='Период обучения')
    description = models.TextField(verbose_name='Описание')
