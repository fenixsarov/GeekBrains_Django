from django.db import models

class Unit(models.Model):
    name = models.CharField(verbose_name=u'Навание', max_length=32, unique=True)
    category = models.ForeignKey('Category')
    # image = models.ImageField(blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)

class Category(models.Model):
    name = models.CharField(verbose_name=u'Название', max_length=16, unique=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    full_name = models.CharField(max_length=20)
# Create your models here.
