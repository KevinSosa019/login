from django.urls import path
from .views import home, products, register, exit


urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('register/', register, name='register'),
    path('logout/', exit, name='exit'),
]