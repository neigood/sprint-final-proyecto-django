from django.db import models
from django.db.models.fields import CharField

# Create your models here.

# codefirst


class Producto(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    precio = models.IntegerField(null=False)


class Caso(models.Model):
    tu_nombre = models.CharField(max_length=50)
    tu_opinion = models.CharField(max_length=50)


opciones_consultas = [
    [0, "conssulta"],
    [1, "reclamo"],
    [2, "sugerencias"],
    [3, "felicitacion"]
]


class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre
