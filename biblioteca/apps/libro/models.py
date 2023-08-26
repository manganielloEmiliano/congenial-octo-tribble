from django.db import models


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autores = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    anio_publicacion = models.PositiveIntegerField()
    editorial = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo
