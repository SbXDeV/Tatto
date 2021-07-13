from django.db import models


# Create your models here.

class WriteToMaster(models.Model):
    """Запись на прием к мастеру"""

    username = models.CharField(max_length=20, verbose_name="Имя клиента")
    number = models.CharField(max_length=28, verbose_name="Номер телефона")
    age = models.IntegerField(verbose_name="Возсраст")

    class Meta:
        """Человекоподный вывод в админке"""
        verbose_name = "Заявки на прием"
        verbose_name_plural = "Заявка на прием"

    def __str__(self):
        """Декоратор для админки"""
        return "Имя клиента: {} \n Номер телефона: {} \n Возраст: {}".format(self.username, self.number, self.age)
