from django.shortcuts import render
from .models import Cliente, Producto, Venta, DetalleVenta
from .forms import VentaForm, DetalleVentaForm
# Create your views here.
def venta(request):
    cliente = Cliente.objects.all()
    producto = Producto.objects.all()
    detalleVentas = DetalleVenta.objects.all()

    if request.method == 'POST':
        venta_form = VentaForm(request.POST)
        detalle_venta_form = DetalleVentaForm(request.POST)
        if venta_form.is_valid() and detalle_venta_form.is_valid():

            venta = venta_form.save()

            detalle_venta = detalle_venta_form.save(commit=False)
            detalle_venta.venta = venta
            detalle_venta.save()
            print("con exito")
        else:
            print("fallamos")
    return render(request, 'ventas.html', {'cliente':cliente, 'producto': producto,'detalleVentas': detalleVentas})

def compra(request):
    return render(request, 'compras.html')