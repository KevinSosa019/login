from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

from .forms import PublicacionForm
from .models import Publicacion


# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def perfil(request):
    return render(request, 'core/perfil.html')

def publicar(request):
    return render(request, 'Venta/PublicarVenta.html')

def Ventas_Publicadas(request):
    return render(request, 'Venta/VentasPublicadas.html')

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

#nuevo
# En tu_aplicacion/views.py


def publicarVenta(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            form.save()
            # Puedes redirigir a una página de éxito o mostrar un mensaje de éxito aquí
            return redirect('/')  # Cambia 'ruta_de_redireccion' por la URL a la que deseas redirigir después de guardar la publicación
    else:
        form = PublicacionForm()
    return render(request,'Venta/publicarVenta.html', {'form': form})

