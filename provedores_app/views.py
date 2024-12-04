from django.shortcuts import render,redirect
from .models import Provedores
# Create your views here.
def inicio_vistaProvedores(request):
    lasmaterias=Provedores.objects.all()
    return render(request,'gestionarProvedores.html',{'mismaterias':lasmaterias})

def registrarProvedores(request):
    id_prov=  request.POST['txtid_prov']
    nombre=  request.POST['txtnombre']
    contacto=  request.POST['txtcontacto']
    telefono=  request.POST['txttelefono']
    direccion= request.POST['txtdireccion']
    tipo_producto= request.POST['txttipo_producto']
    calificacion= request.POST['txtcalificacion']

    guardarmateria=Provedores.objects.create(id_prov=id_prov,nombre=nombre,contacto=contacto, telefono=telefono, direccion=direccion, tipo_producto=tipo_producto, calificacion=calificacion)
    return redirect("/")

def seleccionarProvedores(request,id_prov):
    materia = Provedores.objects.get(id_prov=id_prov)
    return render(request,'editarProvedores.html',{'mismaterias':materia})

def editarProvedores(request):
    id_prov=  request.POST['txtid_prov']
    nombre=  request.POST['txtnombre']
    contacto=  request.POST['txtcontacto']
    telefono=  request.POST['txttelefono']
    direccion= request.POST['txtdireccion']
    tipo_producto= request.POST['txttipo_producto']
    calificacion= request.POST['txtcalificacion']
    materia = Provedores.objects.get(id_prov=id_prov)
    materia.nombre=nombre
    materia.contacto=contacto
    materia.telefono=telefono
    materia.direccion=direccion
    materia.tipo_producto=tipo_producto
    materia.calificacion=calificacion

    materia.save()
    return redirect("/")

def borrarProvedores(request,id_prov):
    materia=Provedores.objects.get(id_prov=id_prov)
    materia.delete()
    return redirect("/")
