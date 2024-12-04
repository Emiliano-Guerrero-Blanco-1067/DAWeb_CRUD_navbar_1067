from django.db import models

# Create your models here.

class Sucursales(models.Model):
    id=models.CharField(primary_key=True,max_length=6)
    direccion= models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    horario=  models.CharField(max_length=100)
    gerente=  models.CharField(max_length=100)
    capacidad= models.PositiveSmallIntegerField()
    estado= models.CharField(max_length=100)
    

    def  __str__(self):
        return self.direccion

