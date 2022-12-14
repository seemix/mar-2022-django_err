# Generated by Django 4.1 on 2022-09-01 14:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_remove_carmodel_body_remove_carmodel_seats_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='brand',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1990), django.core.validators.MaxLengthValidator(2022)]),
        ),
    ]
