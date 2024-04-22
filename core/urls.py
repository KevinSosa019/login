from django.urls import path
from .views import home, nosotros, register, exit, perfil, publicar
from . import views
from django.conf import settings
from django.conf.urls.static import static


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
    path('detallePublicacion/<str:codigo>', views.detalle_publicacion, name='detalle_publicacion'),
    path('ver_perfil_vendedor/<int:vendedor_id>/', views.ver_perfil_vendedor, name='ver_perfil_vendedor'),
    path('enviar_mensaje/<int:vendedor_id>/', views.enviar_mensaje, name='enviar_mensaje'),
    path('mensajes_enviados/<int:vendedor_id>/', views.mensajes_enviados, name='mensajes_enviados'),
    path('mensajes_recibidos/<int:vendedor_id>/', views.mensajes_recibidos, name='mensajes_recibidos'),
    path('denunciar/<int:vendedor_id>/', views.denunciar, name='denunciar'),
    #Buscar
# URLs en tu archivo urls.py
    path('buscar/', views.listarPublicacion, name='buscar'),  # Usa un nombre de URL único para esta vista
  #  path('buscar/', views.busquedaPublicaciones, name='buscar'),
    
    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)