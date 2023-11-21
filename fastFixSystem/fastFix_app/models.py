from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, default='')
    apellido = models.CharField(max_length=200, default='') 
    telefono = models.CharField(max_length=200, default='')
    correo = models.EmailField(max_length=254, default='')
    contraseña= models.CharField(max_length=100, default='')

    class Meta:
     db_table= 'cliente'

      
class Empleado(models.Model):
     nombreEmpresa= models.CharField(max_length=100, default='')
     infoEmpresa= models.CharField(max_length=1000, default='')
     ubicacionEmpresa= models.CharField(max_length=100, default='')
     contactoEmpresa= models.CharField(max_length=100, default='')
     horario= models.CharField(max_length=100, default='')
     estadoEmpresa= models.BooleanField(default=False)
     contraseña= models.CharField(max_length=100, default='')
     
     class Meta:
         db_table='empleado'


class Servicio(models.Model):
        nombreServicio= models.CharField(max_length=100, default='DEFAULT VALUE')
        descripcionServicio= models.CharField(max_length=1000, default='DEFAULT VALUE')
        empresa = models.ForeignKey(Empleado, on_delete=models.CASCADE)

        class Meta:
            db_table='servicio'


class Reserva_servicio(models.Model):
    servicio= models.ForeignKey(Servicio, on_delete=models.CASCADE)
    reserva= models.ForeignKey(Cliente, on_delete=models.CASCADE)


    class Meta:
        db_table='reserva_servicio'


class Reserva(models.Model):
    cliente= models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empresa= models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha= models.DateField()
    estado= models.BooleanField(default=False)
    
    class Meta:
        db_table='reserva'



