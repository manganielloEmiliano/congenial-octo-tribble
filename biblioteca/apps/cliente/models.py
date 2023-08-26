from django.db import models
from ..libro.models import Libro




class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Prestamo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Prestamo de {self.libro.titulo} a {self.cliente.nombre} {self.cliente.apellido}"
