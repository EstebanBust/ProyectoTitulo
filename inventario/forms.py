from django.forms import ModelForm
from .models import Proveedor,Cliente,Producto,FlujoCaja

class CrearProvForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre','rut', 'direccion', 'rubro', 'medioDePago']
        
class CrearClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre','rut', 'direccion']
        
class CrearProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','marca', 'tipo', 'descripcion', 'cantidad', 'proveedor']

class FlujoCajaForm(ModelForm):
    class Meta:
        model= FlujoCaja
        fields = ['concepto', 'tipo_transaccion', 'monto','saldo_actual']