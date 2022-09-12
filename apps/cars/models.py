from django.db import models
from django.core import validators as v
from datetime import date
from apps.autoparks.models import AutoParkModel


# """Створити модель Car з такими полями:
# - марка машини
# - рік випуску
# - кількість місць
# - тип кузову
# - об'єм двигуна (float)"""


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=20, validators=(v.MinLengthValidator(2),))
    year = models.IntegerField(validators=(v.MinValueValidator(1990), v.MaxValueValidator(date.today().year)))
    engine = models.FloatField()
    price = models.IntegerField()
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
