# Generated by Django 2.1.1 on 2018-09-20 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_auto_20180920_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='NombreCategoria',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='NombreGrupo',
            field=models.CharField(max_length=50),
        ),
    ]
