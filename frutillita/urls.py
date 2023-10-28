"""
URL configuration for frutillita project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inventario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name ='home'),
    path('signup/', views.signup, name='signup'),
    path('req/', views.req, name='req'),
    path('logout/', views.signout, name='signout'),
    path('signin/', views.signin, name='signin'),
    path('req/proveedor/', views.create_proveedor, name='create_proveedor'),
    path('req/cliente/', views.create_cliente, name='create_cliente'),
    path('req/producto/', views.create_producto, name='create_producto'),
    #path('create/', views.create, name='create'),
    path('req/buscaProducto/', views.busca_producto, name='busca_productos'),
    path('req/buscaProveedor/', views.busca_proveedor, name='busca_proveedor'),
    path('req/buscaCliente/', views.busca_cliente, name='busca_cliente'),
    path('req/buscaProducto/mostrarProducto/<int:producto_id>/', views.mostrarProducto, name='mostrar_producto'),
    path('req/buscaProducto/mostrarProveedor/<int:proveedor_id>/', views.mostrarProveedor, name='mostrar_proveedor'),
    path('req/buscaProducto/mostrarCliente/<int:cliente_id>/', views.mostrarCliente, name='mostrar_cliente'),
    path('req/buscaProducto/mostrarProveedor/<int:proveedor_id>/delete', views.deleteProveedor, name='delete_proveedor'),
    path('req/buscaProducto/mostrarProducto/<int:producto_id>/delete', views.deleteProducto, name='delete_producto'),
    path('req/buscaProducto/mostrarCliente/<int:cliente_id>/delete', views.deleteCliente, name='delete_cliente'),
    path('caja/', views.caja, name='caja'),
    path('caja/detalle/<int:caja_id>/', views.detalle_caja, name='detalle_caja'),
    path('caja/crear_flujo_de_caja', views.caja, name='crear_flujo_caja'),
    path('caja/modificar_flujo_de_caja/<int:caja_id>', views.modificar_caja, name='modificar_flujo_caja'),
    path('caja/borrar_Flujo_de_caja/<int:caja_id>', views.borrarCaja, name='borrar_flujo_caja'),
    path('ventas/', views.borrarCaja, name='venta'),
    path('compras/', views.borrarCaja, name='compra'),
]