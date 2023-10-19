# Generated by Django 4.2.6 on 2023-10-19 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_flujocaja'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flujocaja',
            name='saldo_anterior',
        ),
        migrations.AlterField(
            model_name='flujocaja',
            name='saldo_actual',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
