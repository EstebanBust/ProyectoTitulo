from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    rubro = models.CharField(max_length=100)
    medioDePago = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.rubro}"


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    cantidad = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class FlujoCaja(models.Model):
    fecha = models.DateField(default=timezone.now)
    concepto = models.CharField(max_length=255)
    tipo_transaccion = models.CharField(
        max_length=10,
        choices=[('Ingreso', 'Ingreso'), ('Egreso', 'Egreso')]
    )
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_actual = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.saldo_actual is None:
            ultima_transaccion = FlujoCaja.objects.last()
            saldo_anterior = ultima_transaccion.saldo_actual if ultima_transaccion else 0
            # Calcula el saldo actual antes de guardar
            if self.tipo_transaccion == 'Ingreso':
                self.saldo_actual = saldo_anterior + self.monto
            else:
                self.saldo_actual = saldo_anterior - self.monto

        super(FlujoCaja, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.fecha} - {self.concepto}"
