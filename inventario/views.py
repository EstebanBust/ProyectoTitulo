from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import CrearProvForm, CrearProductoForm, CrearClienteForm, FlujoCajaForm
from .models import Producto, Proveedor, Cliente, FlujoCaja
from django.db.models import Q, Sum, F
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


def req(request):
    return render(request, 'req.html',)


def home(request):
    return render(request, 'home.html',)

# Sesiones y loggin


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
                    username=request.POST['username'], email=request.POST['email'], password=request.POST['password1'])
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

# insertar registros


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
        proveedores = Proveedor.objects.all()
        return render(request, 'create_producto.html', {'form': CrearProductoForm(), 'proveedores': proveedores})

    else:
        form = CrearProductoForm(request.POST)
        form.save()
        return render(request, 'create_producto.html', {'form': CrearProductoForm()})


# Busqueda y listas
@login_required
def busca_producto(request):
    if request.method == 'POST':
        categoria = request.POST.get('categoria')
        imput = request.POST.get('imput')
        # Filtra los productos según la categoría seleccionada
        if categoria:
            productos = Producto.objects.filter(
                Q(**{f'{categoria}__icontains': imput}))
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
            proveedor = Proveedor.objects.filter(
                Q(**{f'{categoria}__icontains': imput}))

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
            cliente = Cliente.objects.filter(
                Q(**{f'{categoria}__icontains': imput}))

        else:
            # Si no se selecciona una categoría, muestra todos los cliente
            cliente = Cliente.objects.all()
        return render(request, 'listaCliente.html', {'clientes': cliente})

    else:
        # Maneja la primera carga del formulario aquí si es necesario
        cliente = Cliente.objects.all()
        return render(request, 'listaCliente.html', {'clientes': cliente})


@login_required
def mostrarProveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, pk=proveedor_id)

    if request.method == 'POST':
        form = CrearProvForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('req')

    else:
        form = CrearProvForm(instance=proveedor)

    return render(request, 'mostrarProveedor.html', {'proveedor': proveedor, 'form': form})


@login_required
def mostrarProducto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)

    if request.method == 'POST':
        form = CrearProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('req')

    else:
        form = CrearProductoForm(instance=producto)
        proveedores = Proveedor.objects.all()

    return render(request, 'mostrarProducto.html', {'producto': producto, 'proveedores': proveedores})


@login_required
def mostrarCliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)

    if request.method == 'POST':
        form = CrearClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('req')
    else:
        form = CrearClienteForm(instance=cliente)

    return render(request, 'mostrarCliente.html', {'cliente': cliente, 'form': form})


# Borrar entradas
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


@login_required
def caja(request):
    flujo_de_caja = FlujoCaja.objects.all()
    saldo_actual = FlujoCaja.objects.last()
    ingresos = FlujoCaja.objects.filter(
        tipo_transaccion='Ingreso').aggregate(total_ingresos=Sum('monto'))
    egresos = FlujoCaja.objects.filter(tipo_transaccion='Egreso').aggregate(
        total_egresos=Sum(F('monto') * -1))
    saldo = ingresos['total_ingresos'] + egresos['total_egresos']

    if request.method == 'POST':
        form = FlujoCajaForm(request.POST)
        if form.is_valid():
            flujo_caja = form.save(commit=False)
            flujo_caja.request_user = request.user  # Asigna el usuario actual
            flujo_caja.save()
    else:
        form = FlujoCajaForm()

    return render(request, 'flujo_de_caja.html', {'flujo_de_cajas': flujo_de_caja, 'form': form, 'saldo_actual': saldo_actual, 'saldo': saldo})


@login_required
def detalle_caja(request, caja_id):
    flujo_de_caja = FlujoCaja.objects.get(id=caja_id)
    form = FlujoCajaForm()
    return render(request, 'detalle_caja.html', {'flujo_de_caja': flujo_de_caja, 'form': form})


@login_required
def modificar_caja(request, caja_id):
    if request.method == 'POST':
        form = FlujoCajaForm(request.POST, instance=caja_id)
        if form.is_valid():
            form.save()

    return redirect('caja')


@login_required
def borrarCaja(request, caja_id):
    caja = get_object_or_404(FlujoCaja, pk=caja_id)
    if request.method == 'POST':
        caja.delete()

    return redirect('caja')
