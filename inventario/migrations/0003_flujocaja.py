# Generated by Django 4.2.6 on 2023-10-19 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_proveedor_mediodepago'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlujoCaja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('concepto', models.CharField(max_length=255)),
                ('tipo_transaccion', models.CharField(choices=[('Ingreso', 'Ingreso'), ('Egreso', 'Egreso')], max_length=10)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('saldo_anterior', models.DecimalField(decimal_places=2, max_digits=10)),
                ('saldo_actual', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]