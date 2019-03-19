# -*- encoding: utf-8 -*-

from django.db import models

from django.contrib.auth.models import User

# Create your models here.
"""class Usuario (models.Model):
	idusuario = models.AutoField(primary_key=True)
	usuario = models.OneToOneField(User)
	nombre = models.CharField(max_length=50)
	apellidos= models.CharField(max_length=50)
	direccion = models.CharField(max_length=80)
	telefono = models.IntegerField()
	#imagen = models.FileField(upload_to='fotos_usuarios')"""

	
							 

	

	#class Meta:
	#	ordering = ('')


class Perfiles(models.Model):
	idperfil = models.AutoField(primary_key=True)
	usuario = models.OneToOneField(User)
	nombre = models.CharField(max_length=50)
	apellidos= models.CharField(max_length=50)
	direccion = models.TextField(max_length=120)
	telefono = models.CharField(max_length=10)

	def __unicode__(self):
		return self.usuario.username

		

class Libro (models.Model):
	idlibro = models.AutoField(primary_key=True)
	nombre_libro = models.CharField( max_length= 100)
	sinopsis = models.CharField(max_length=400)
	editorial = models.CharField(max_length=50)
	autor = models.CharField(max_length=80)
	genero = models.CharField(max_length=15)
	pais_autor  = models.CharField(max_length=50)
	fecha_publicacion = models.DateField(auto_now_add=True)
	paginas = models.IntegerField()
	imagen = models.FileField(upload_to='images')
	estado = models.BooleanField()

							 

	def __unicode__(self):
		return 'NOMBRE DE LIBRO : %s EDITORIAL : %s' %(self.nombre_libro ,self.editorial)

		#class Meta:
			#ordering = ('nombre_libro')

	def traer_url_imagen(self):
		return 'http://localhost:8000/media/%s' % self.imagen


class Prestamo (models.Model):
	idprestamo = models.AutoField(primary_key=True)
	idlibro = models.ForeignKey(Libro)
	idperfil = models.ForeignKey(Perfiles)
	tiempo_registro = models.DateField(auto_now=True)
	fecha_devolucion=models.DateField()
							 

	def __unicode__(self):
		return 'ID PRESTAMO: %s FECHA DE DEVOLUCION : %s' %(self.idprestamo ,self.fecha_devolucion)
		
		#class Meta:
		#	ordering = ('fecha_salida','fecha_devolucion')

