# Generated by Django 2.1.1 on 2018-09-20 13:53

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False)),
                ('NombreCategoria', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('idGrupo', models.IntegerField(primary_key=True, serialize=False)),
                ('NombreGrupo', models.TextField()),
                ('Visibilidad', models.BooleanField(default=True)),
                ('NecesitaInvitacion', models.BooleanField(default=False)),
                ('FechaCreacionG', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('FechaBajaG', models.DateField(default=None)),
                ('FechaModiG', models.DateField(default=None)),
                ('CategoriaGrupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.Categoria')),
                ('Creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('idPublicacion', models.IntegerField(primary_key=True, serialize=False)),
                ('Contenido', models.TextField()),
                ('Titulo', models.TextField()),
                ('FechaPublicacion', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('FechaBajaPublicacion', models.DateField(default=None)),
                ('FechaModiPublicacion', models.DateField(default=None)),
                ('idGrupoPu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.Grupo')),
                ('idUserPublico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserGrupos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idGrupoUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.Grupo')),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]