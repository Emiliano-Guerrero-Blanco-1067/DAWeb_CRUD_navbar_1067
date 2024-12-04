from django.db import models

# Create your models here.

class Facturas(models.Model):
    id_fac= models.CharField(primary_key=True,max_length=6)
    total= models.PositiveSmallIntegerField()
    area=  models.CharField(max_length=100)
    estado=  models.CharField(max_length=100)
    fecha= models.DateField()
    met_pago= models.CharField(max_length=100)
    id_suc= models.CharField(max_length=100)
    id_prod= models.CharField(max_length=100)
    id_cli= models.CharField(max_length=100)
    id_emp= models.CharField(max_length=100)

    def  __str__(self):
        return self.area
