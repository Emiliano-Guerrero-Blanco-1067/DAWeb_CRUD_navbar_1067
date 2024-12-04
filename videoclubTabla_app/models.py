from django.db import models

# Create your models here.

class Productos(models.Model):
    codigo= models.CharField(primary_key=True,max_length=6)
    nombre = models.CharField(max_length=100)
    creditos=  models.PositiveSmallIntegerField()
    creditos1=  models.PositiveSmallIntegerField()
    fecha= models.DateField()
    descripcion= models.CharField(max_length=100)
    provedor_id= models.CharField(max_length=100)

    def  __str__(self):
        return self.nombre

