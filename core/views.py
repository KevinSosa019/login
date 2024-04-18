from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .models import Publicacion
from django.contrib import messages
from datetime import datetime
from django.db.models import Q



# Create your views here.

#Mostrar las publicaiones al inicio 
def home(request):
    publicacionesListados = Publicacion.objects.all()
    return render(request, "core/home.html", {"publicaciones": publicacionesListados})


def nosotros(request):
    return render(request, 'core/nosotros.html')

def perfil(request):
    return render(request, 'core/perfil.html')


"""@login_required
def products(request):
    return render(request, 'core/products.html')"""

def exit(request):
    logout(request)
    return redirect('home')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)


#1Publicaciones
def publicar(request):
    publicacionesListados = Publicacion.objects.all()
    messages.success(request, 'Publicacion listada!')
    return render(request, "Venta/PublicarVenta.html", {"publicaciones": publicacionesListados})
#2da
def registrarPublicacion(request):
    codigo = request.POST['txtCodigo']
    titulo = request.POST['txtTitulo']
    precio = request.POST['numPrecio']
    
    cantidad = request.POST['numCantidad']
    unidad = request.POST['txtUnidad']
    categoria = request.POST['txtCategoria']
  #  fechaCosecha = request.POST['DateFechaCosecha'] 
    descripcion = request.POST['txtDescripcion']
    

    publicacion = Publicacion.objects.create(
        codigo=codigo, 
        titulo=titulo, 
        precio=precio,
        cantidad=cantidad,
        unidad=unidad,
        categoria=categoria,
   #     fechaCosecha=fechaCosecha,
        descripcion=descripcion   )
    
  
    messages.success(request, 'Publicacion registrada!')
    return redirect('/publicar')

def edicionPublicacion(request, codigo):
    publicacion = Publicacion.objects.get(codigo=codigo)
    return render(request, "Venta/edicionPublicacion.html", {"publicacion": publicacion})


def editarPublicacion(request):
    codigo = request.POST['txtCodigo']
    titulo = request.POST['txtTitulo']
    precio = request.POST['numPrecio']
    cantidad = request.POST['numCantidad']
    unidad = request.POST['txtUnidad']
    categoria = request.POST['txtCategoria']
 #   fechaCosecha = request.POST['DateFechaCosecha']
    descripcion = request.POST['txtDescripcion']

    publicacion = Publicacion.objects.get(codigo=codigo)
    publicacion.titulo = titulo
    publicacion.precio = precio
    publicacion.cantidad = cantidad
    publicacion.unidad = unidad
    publicacion.categoria = categoria
   # publicacion.fechaCosecha = fechaCosecha
    publicacion.descripcion = descripcion
    publicacion.save()

    messages.success(request, 'Publicacion actualizada!')
    return redirect('/publicar')


def eliminarPublicacion(request, codigo):
    publicacion = Publicacion.objects.get(codigo=codigo)
    publicacion.delete()

    messages.success(request, 'Publicacion eliminada!')
    return redirect('/publicar')

#Buscar
def buscar(request):
    publicacionesListados = Publicacion.objects.all()
    return render(request, "core/buscar.html", {"publicaciones": publicacionesListados})

def busquedaPublicaciones(request):
    busqueda = request.POST.get("buscar")
    publicacionesListados = Publicacion.objects.all()

    if busqueda:
        publicacionesListados = Publicacion.objects.filter(
            Q(titulo__icontains = busqueda) | 
            Q(categoria__icontains = busqueda)  
        ).distinct()
         

    return render(request, 'busqueda.html', {'busqueda':busqueda})

