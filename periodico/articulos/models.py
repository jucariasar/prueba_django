from django.db import models

# Create your models here.
class Reportero(models.Model):
	nombres = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=100)

	def __str__(self):
		return

class Articulo(models.Models):
	fecha_publicacion = models.DateTimeField('Fecha de Puclicacion')
	Prueba


