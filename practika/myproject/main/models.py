from django.db import models


class Service(models.Model):
    name = models.CharField('Имя', max_length=50)
    price = models.IntegerField('Цена', max_length=50)
    ind = models.CharField('Индекс', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'