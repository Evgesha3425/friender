from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50, verbose_name='имя')
    surname = models.CharField(max_length=50, verbose_name='фамилия')
    age = models.IntegerField(verbose_name='возраст')
    gender = models.CharField(max_length=1, verbose_name='пол')
    looking_gender = models.CharField(max_length=1, verbose_name='ищу')

    def __str__(self):
        return self.name


class Establishment(models.Model):
    name_est = models.CharField(max_length=100, verbose_name='название')
    address = models.CharField(max_length=150, verbose_name='адрес')
    price = models.IntegerField(verbose_name='ценовая категория')

    def __str__(self):
        return self.name_est