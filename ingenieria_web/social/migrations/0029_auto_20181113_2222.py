# Generated by Django 2.1.3 on 2018-11-14 01:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0028_perfil_universidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuspensionUsuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(blank=True, max_length=100, null=True)),
                ('fechaSuspension', models.DateField(default=datetime.date.today, editable=False)),
                ('duracion', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='perfil',
            name='carrera',
            field=models.CharField(blank=True, default='Agregar Carrera', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='localizacion',
            field=models.CharField(blank=True, default='Agregar Ubicacion', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='nombreCompleto',
            field=models.CharField(blank=True, default='Agregar Nombre', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='universidad',
            field=models.CharField(blank=True, default='Agregar Universidad', max_length=100, null=True),
        ),
    ]