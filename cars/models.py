from django.db import models

"""Створити модель Car з такими полями:
- марка машини
- рік випуску
- кількість місць
- тип кузову
- об'єм двигуна (float)"""


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=20)
    year = models.IntegerField()
    seats = models.IntegerField()
    body = models.CharField(max_length=20)
    engine = models.FloatField()
