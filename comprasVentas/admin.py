from django.contrib import admin
from .models import Venta, DetalleVenta, Compra, DetalleCompra
# Register your models here.
admin.site.register(Venta)
admin.site.register(DetalleVenta)
admin.site.register(Compra)
admin.site.register(DetalleCompra)
