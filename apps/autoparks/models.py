from django.db import models


# Create your models here.
class AutoParkModel(models.Model):
    class Meta:
        db_table = 'auto_parks'
    name = models.CharField(max_length=20)
