# Generated by Django 4.2.6 on 2023-10-19 09:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0005_flujocaja_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flujocaja',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
