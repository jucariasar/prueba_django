from django.db import models

# Create your models here.
class Reportero(models.Model):
	nombres = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=100)

	def setNombres(self, nombres):
		self.nombres = nombres

	def getNombres(self):
		return self.nombres

	def setApellidos(self, apellidos):
		self.apellidos = apellidos

	def getApellidos(self):
		return self.apellidos

	def __str__(self):
		return self.getNombres() + ' ' + self.getApellidos()

class Articulo(models.Models):
	fecha_publicacion = models.DateTimeField('Fecha de Puclicacion')
	encabezado = CharField(max_length=200)
	contenido = TextField()
	reportero = models.ForeignKey(Reportero, on_delete=model.CASCADE)

	def setFechaPublicacion(self, fecha):
		self.fecha = fecha

	def getFechaPublicacion(self):
		return self.fecha_publicacion

	def setEncabezado(self, encabezado):
		self.encabezado = encabezado

	def getEncabezado(self):
		return self.encabezado

	def setContenido(self, contenido):
		self.contenido = contenido

	def getContenido(self):
		return self.contenido

	def setReportero(self, reportero):
		self.reportero = reportero

	def getReportero(self):
		return self.reportero

	def __str__(self):
		return self.getEncabezado()