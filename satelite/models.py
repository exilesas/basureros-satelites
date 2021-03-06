# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Imagen(models.Model):
	imagen = models.FileField(upload_to="media")
	reporte = models.ForeignKey('Reporte')
	class Meta:
		verbose_name = "Imagen"
		verbose_name_plural = "Imágenes"
	#end class
	
	def __unicode__(self):
		return unicode(self.reporte)
	#end def
#end class

class GPS(models.Model):
	latitude = models.CharField(max_length=50)
	longitude = models.CharField(max_length=50)
	class Meta:
		verbose_name = "GPS"
		verbose_name_plural = "GPS's"
	#end class

	def __unicode__(self):
		return unicode(self.latitude) + ", " + unicode(self.longitude)
	#end def
#end class

class Reporte(models.Model):
	gps = models.OneToOneField('GPS')
	fecha = models.DateTimeField(auto_now_add=True)
	basurero = models.ForeignKey('Basurero', null = True, blank = True)
	descartado = models.NullBooleanField(default=None)
	clasificador = models.ForeignKey(User, null=True, blank=True)
	class Meta:
		verbose_name = "Reporte"
		verbose_name_plural = "Reportes"
	#end class

	def __unicode__(self):
		return  "reporte " + unicode(self.pk) + ' ' + self.fecha.strftime('%d/%m/%Y')
	#end def
#end class

class Basurero(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField()
	gps = models.OneToOneField('GPS')
	fecha = models.DateTimeField(auto_now_add=True)
	tamano = models.FloatField()
	class Meta:
		verbose_name = "Basurero"
		verbose_name_plural = "Basureros"
	#end class

	def __unicode__(self):
		return unicode(self.nombre)
	#end def

	def imagenes(self):
		return Imagen.objects.filter(reporte__basurero__id=self.id)
	#end def
#end class
