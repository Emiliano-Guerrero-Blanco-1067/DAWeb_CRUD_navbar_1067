from django.shortcuts import render,redirect
from .models import Sucursales
# Create your views here.
def inicio_vistaSucursales(request):
    lasmaterias=Sucursales.objects.all()
    return render(request,'gestionarSucursales.html',{'mismaterias':lasmaterias})

def registrarSucursales(request):
    id=request.POST['txtid']
    direccion=  request.POST['txtdireccion']
    telefono=  request.POST['txttelefono']
    horario=  request.POST['txthorario']
    gerente=  request.POST['txtgerente']
    capacidad= request.POST['numcapacidad']
    estado= request.POST['txtestado']
    

    guardarmateria=Sucursales.objects.create(direccion=direccion,telefono=telefono,horario=horario, gerente=gerente, capacidad=capacidad, estado=estado, id=id)
    return redirect("/")

def seleccionarSucursales(request,id):
    materia = Sucursales.objects.get(id=id)
    return render(request,'editarSucursales.html',{'mismaterias':materia})

def editarSucursales(request):
    id=  request.POST['txtid']
    direccion=  request.POST['txtdireccion']
    telefono=  request.POST['txttelefono']
    horario=  request.POST['txthorario']
    gerente= request.POST['txtgerente']
    capacidad= request.POST['numcapacidad']
    estado= request.POST['txtestado']
    materia = Sucursales.objects.get(id=id)
    materia.direccion=direccion
    materia.telefono=telefono
    materia.horario=horario
    materia.gerente=gerente
    materia.capacidad=capacidad
    materia.estado=estado

    materia.save()
    return redirect("/")

def borrarSucursales(request,id):
    materia=Sucursales.objects.get(id=id)
    materia.delete()
    return redirect("/")
