from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import CrearProvForm, CrearProductoForm, CrearClienteForm
from .models import Producto, Proveedor, Cliente
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


def req(request):
    return render(request, 'req.html',)


def home(request):
    return render(request, 'home.html',)

#Sesiones y loggin
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # registrar usuario
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('req')

            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'})

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'})


def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {'form': AuthenticationForm})

    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {'form': AuthenticationForm, 'error': 'Usuario o contraseña incorrecta'})
        else:
            login(request, user)
            return redirect('home')




#insertar registros
@login_required
def create_proveedor(request):
    if request.method == 'GET':
        return render(request, 'create_proveedor.html', {'form': CrearProvForm()})

    else:
        form = CrearProvForm(request.POST)
        form.save()
        return render(request, 'create_proveedor.html', {'form': CrearProvForm()})
    
@login_required
def create_cliente(request):
    if request.method == 'GET':
        return render(request, 'create_cliente.html', {'form': CrearClienteForm()})

    else:
        form = CrearClienteForm(request.POST)
        form.save()
        return render(request, 'create_cliente.html', {'form': CrearClienteForm()})
    

@login_required
def create_producto(request):
    if request.method == 'GET':
        return render(request, 'create_producto.html', {'form': CrearProductoForm()})

    else:
        form = CrearProductoForm(request.POST)
        form.save()
        return render(request, 'create_producto.html', {'form': CrearProductoForm()})


#Busqueda y listas
@login_required
def busca_producto(request):
    if request.method == 'POST':
        categoria = request.POST.get('categoria')
        imput = request.POST.get('imput')
        # Filtra los productos según la categoría seleccionada
        if categoria:
            productos = Producto.objects.filter(Q(**{categoria: imput}))
        else:
            # Si no se selecciona una categoría, muestra todos los productos
            productos = Producto.objects.all()

        return render(request, 'listaProductos.html', {'productos': productos})
    else:
        # Maneja la primera carga del formulario aquí si es necesario
        productos = Producto.objects.all()
        return render(request, 'listaProductos.html', {'productos': productos})
    
@login_required
def busca_proveedor(request):
    if request.method == 'POST':
        categoria = request.POST.get('categoria')
        imput = request.POST.get('imput')

        # Filtra los productos según la categoría seleccionada
        if categoria:
            proveedor = Proveedor.objects.filter(Q(**{categoria: imput}))

        else:
            # Si no se selecciona una categoría, muestra todos los proveedor
            proveedor = Proveedor.objects.all()
        return render(request, 'listaProveedor.html', {'proveedores': proveedor})

    else:
        # Maneja la primera carga del formulario aquí si es necesario
        proveedor = Proveedor.objects.all()
        return render(request, 'listaProveedor.html', {'proveedores': proveedor})
    
@login_required
def busca_cliente(request):
    if request.method == 'POST':
        categoria = request.POST.get('categoria')
        imput = request.POST.get('imput')

        # Filtra los productos según la categoría seleccionada
        if categoria:
            cliente = Cliente.objects.filter(Q(**{categoria: imput}))

        else:
            # Si no se selecciona una categoría, muestra todos los cliente
            cliente = Cliente.objects.all()
        return render(request, 'listaCliente.html', {'clientes': cliente})

    else:
        # Maneja la primera carga del formulario aquí si es necesario
        cliente = Cliente.objects.all()
        return render(request, 'listaCliente.html', {'clientes': cliente})

#detalle y editar entradas
@login_required
def mostrarProveedor(request, proveedor_id):
    if request.method == 'GET':
        proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
        form = CrearProvForm(instance=proveedor)
        return render(request, 'mostrarProveedor.html', {'proveedor': proveedor, 'form': form})
    else:
        proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
        form = CrearProvForm(request.POST, instance=proveedor)
        form.save()
        return redirect('req')
    
@login_required
def mostrarProducto(request, producto_id):
    if request.method == 'GET':
        producto = get_object_or_404(Producto, pk=producto_id)
        form = CrearProductoForm(instance=producto)
        return render(request, 'mostrarProducto.html', {'producto': producto, 'form': form})
    else:
        producto = get_object_or_404(Producto, pk=producto_id)
        form = CrearProductoForm(request.POST, instance=producto)
        form.save()
        return redirect('req')
    
@login_required
def mostrarCliente(request, cliente_id):
    if request.method == 'GET':
        cliente = get_object_or_404(Cliente, pk=cliente_id)
        form = CrearClienteForm(instance=cliente)
        return render(request, 'mostrarCliente.html', {'cliente': cliente, 'form': form})
    else:
        cliente = get_object_or_404(Cliente, pk=cliente_id)
        form = CrearClienteForm(request.POST, instance=cliente)
        form.save()
        return redirect('req')


#Borrar entradas
@login_required
def deleteProveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('req')
    
@login_required    
def deleteProducto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('req')
    
@login_required    
def deleteCliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('req')
