from django.urls import path
from .views import home, nosotros, register, exit, perfil, publicar 
from . import views


urlpatterns = [
    path('', home, name='home'),
    path('nosotros/',nosotros, name='nosotros'),
    path('perfil/',perfil, name='perfil'),
    path('publicar/',publicar, name='publicar'),
    path('register/', register, name='register'),
    path('logout/', exit, name='exit'),
  
    #publicacion
    path('registrarPublicacion/', views.registrarPublicacion),
    path('publicar/edicionPublicacion/<codigo>', views.edicionPublicacion),
    path('editarPublicacion/', views.editarPublicacion),
    path('publicar/eliminarPublicacion/<codigo>', views.eliminarPublicacion),

]