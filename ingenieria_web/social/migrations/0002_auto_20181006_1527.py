# Generated by Django 2.1.1 on 2018-10-06 18:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='FechaCreacionG',
            field=models.DateField(default=datetime.date.today, editable=False, verbose_name='Fecha Creacion'),
        ),
    ]
