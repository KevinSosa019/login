from django.urls import path
from .views import home, nosotros, register, exit, perfil, publicar, Ventas_Publicadas 
from . import views


urlpatterns = [
    path('', home, name='home'),
    path('nosotros/',nosotros, name='nosotros'),
    path('perfil/',perfil, name='perfil'),
    path('Ventas_Publicadas/',Ventas_Publicadas, name='Ventas_Publicadas'),
    path('publicar/',publicar, name='publicar'),
    path('register/', register, name='register'),
    path('logout/', exit, name='exit'),
  
    #publicacion
    path('registrarPublicacion/', views.registrarPublicacion),
    path('publicar/edicionPublicacion/<codigo>', views.edicionPublicacion),
    path('editarPublicacion/', views.editarPublicacion),
    path('publicar/eliminarPublicacion/<codigo>', views.eliminarPublicacion),

]