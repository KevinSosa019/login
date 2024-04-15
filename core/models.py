from django.db import models

# Create your models he
# En tu_aplicacion/models.py

# Define las opciones para el campo 'opciones'
OPCIONES_CHOICES = [
    ('nuevo', 'Nuevo'),
    ('usado', 'Usado'),
    ('danado', 'Dañado'),
]

class Publicacion(models.Model):
    titulo = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField()
    opciones = models.CharField(max_length=50, choices=OPCIONES_CHOICES)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo


