# Generated by Django 4.1 on 2022-09-01 13:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carmodel',
            name='body',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='seats',
        ),

        migrations.AddField(
            model_name='carmodel',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
