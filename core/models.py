
from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Publicacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    codigo = models.CharField(primary_key=True, max_length=6)
    titulo = models.CharField(max_length=100, default='Título Predeterminado')
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    cantidad = models.IntegerField(default=0)  
    unidad = models.CharField(max_length=10, choices=[('Kg', 'Kg'), ('g', 'g'), ('L', 'L')], default='Kg')  
    categoria = models.CharField(max_length=100, choices=[('Vegetales', 'Vegetales'), ('Frutas', 'Frutas'), ('Hierbas', 'Hierbas')], default='Vegetales')  # Ejemplo de valor predeterminado
  #  fechaCosecha = models.DateField(default=date.today)
    descripcion = models.TextField(default='Descripción predeterminada')  
    
    class Meta:
      verbose_name = 'Publicacion'
      verbose_name_plural = 'Publicaciones'
      ordering = ['codigo']

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.precio)
 
 