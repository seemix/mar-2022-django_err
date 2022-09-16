from datetime import date

from django.core import validators as v
from django.db import models

from apps.autoparks.models import AutoParkModel

from .managers import CarManager
from .services import upload_to

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
    photo = models.ImageField(upload_to=upload_to, blank=True)
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CarManager()