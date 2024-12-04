from django.db import models

# Create your models here.

class Empleados(models.Model):
    id_emp= models.CharField(primary_key=True,max_length=6)
    nombre = models.CharField(max_length=100)
    apellido=  models.CharField(max_length=100)
    puesto=  models.CharField(max_length=100)
    fecha_contratacion= models.DateField()
    salario_quincena= models.PositiveSmallIntegerField()
    dni= models.CharField(max_length=100)
    id_suc= models.CharField(max_length=100)

    def  __str__(self):
        return self.nombre
