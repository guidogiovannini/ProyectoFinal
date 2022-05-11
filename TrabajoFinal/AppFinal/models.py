from django.db import models
import datetime

# Create your models here.
class Empleado(models.Model):
	Documento=models.IntegerField()
	Nombre=models.CharField(max_length=50)
	Apellido=models.CharField(max_length=50)
	Telefono= models.IntegerField()
	Contacto= models.EmailField()
	def __str__(self):
		return f'{self.Documento} {self.Nombre} {self.Apellido} {self.Telefono} {self.Contacto}'

class Conductor(models.Model):
	Documento= models.IntegerField()
	Nombre= models.CharField(max_length=50)
	Apellido= models.CharField(max_length=50)
	Telefono= models.IntegerField()
	Contacto= models.EmailField()
	def __str__(self):
		return f'{self.Documento} {self.Nombre} {self.Apellido} {self.Telefono} {self.Contacto}'

class Camion(models.Model):
	Patente = models.CharField(max_length=7)
	Marca= models.CharField(max_length=50)
	Color= models.CharField(max_length=50)
	TipoCarga= models.CharField(max_length=50)
	def __str__(self):
		return f'{self.Patente} {self.Marca} {self.Color} {self.TipoCarga}'
