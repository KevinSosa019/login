from django.urls import path
from .views import home, nosotros, register, exit, perfil, publicar
from . import views


urlpatterns = [
     #inicio
    path('', views.home, name='home'),
    path('nosotros/',nosotros, name='nosotros'),
    path('perfil/',perfil, name='perfil'),
    path('publicar/',publicar, name='publicar'),
    path('register/', register, name='register'),
    path('logout/', exit, name='exit'),
  
    #publicacion
    #están diseñadas para manejar solicitudes HTTP y realizar operaciones en el backend
    path('registrarPublicacion/', views.registrarPublicacion),
    path('publicar/edicionPublicacion/<codigo>', views.edicionPublicacion),
    path('editarPublicacion/', views.editarPublicacion),
    path('publicar/eliminarPublicacion/<codigo>', views.eliminarPublicacion),
    
    #Buscar
# URLs en tu archivo urls.py
    path('buscar/', views.listarPublicacion, name='buscar'),  # Usa un nombre de URL único para esta vista
  #  path('buscar/', views.busquedaPublicaciones, name='buscar'),
    
    


]