# Generated by Django 2.1.2 on 2018-10-14 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0009_auto_20181011_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermanager',
            name='avatar',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
