# Generated by Django 2.1.3 on 2018-11-09 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0022_auto_20181109_1123'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CategoriaUsuario',
        ),
        migrations.RemoveField(
            model_name='usergrupos',
            name='Permisos',
        ),
        migrations.AddField(
            model_name='usergrupos',
            name='Rango',
            field=models.IntegerField(choices=[(1, 'Normal'), (2, 'Moderador'), (3, 'Administrador')], default=1),
        ),
        migrations.DeleteModel(
            name='Permisos',
        ),
    ]
