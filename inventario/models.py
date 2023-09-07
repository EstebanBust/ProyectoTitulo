from django.db import models


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
