from django.db import models

# Create your models here.

class Provedores(models.Model):
    id_prov= models.CharField(primary_key=True,max_length=6)
    nombre = models.CharField(max_length=100)
    contacto=  models.CharField(max_length=100)
    telefono= models.CharField(max_length=100)
    direccion= models.CharField(max_length=100)
    tipo_producto= models.CharField(max_length=100)
    calificacion= models.CharField(max_length=100)

    def  __str__(self):
        return self.nombre

