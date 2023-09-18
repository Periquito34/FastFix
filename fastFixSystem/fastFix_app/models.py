from django.db import models

# Create your models here.

class Cliente(models.Model):
    idcliente = models.IntegerField(default='DEFAULT VALUE')
    nombre = models.CharField(max_length=100, default='DEFAULT VALUE')
    apellido = models.CharField(max_length=200, default='DEFAULT VALUE') 
    correo = models.EmailField(max_length=254, default='DEFAULT VALUE')
    dirrecion = models.CharField(max_length=200, default='DEFAULT VALUE')

    class Meta:
     db_table= 'cliente'

class CategoriaServicio(models.Model):
      tipo = models.CharField(max_length=200, default='DEFAULT VALUE')
      empresaAsociada = models.CharField(max_length=200, default='DEFAULT VALUE')

      class Meta:
          db_table= 'categoriaservicio'
      
class Solicitud(models.Model):
      solicitudId = models.IntegerField(default='DEFAULT VALUE')
      categoriaSolicitud = models.CharField(max_length=200, default='DEFAULT VALUE')
      disponibilidad= models.BooleanField()

      class Meta:
          db_table='solicitud'
      
class Empleado(models.Model):
     idempresa = models.IntegerField(default='DEFAULT VALUE')
     nombreEmpresa= models.CharField(max_length=100, default='DEFAULT VALUE')
     ubicacionEmpresa= models.CharField(max_length=100, default='DEFAULT VALUE')
     infoEmpresa= models.CharField(max_length=1000, default='DEFAULT VALUE')
     estadoEmpresa= models.BooleanField()
     categoriaServicio= models.CharField(max_length=100, default='DEFAULT VALUE')

     class Meta:
         db_table='empleado'



