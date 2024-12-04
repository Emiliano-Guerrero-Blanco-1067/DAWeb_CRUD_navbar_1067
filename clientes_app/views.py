from django.shortcuts import render,redirect
from .models import Clientes
# Create your views here.
def inicio_vistaClientes(request):
    lasclientes=Clientes.objects.all()
    return render(request,'gestionarClientes.html',{'misclientes':lasclientes})

def registrarCliente(request):
    id_cli=  request.POST['txtid_cli']
    nombre=  request.POST['txtnombre']
    apellido=  request.POST['txtapellido']
    correo=  request.POST['txtcorreo']
    fecha= request.POST['txtfecha']
    telefono= request.POST['txttelefono']
    direccion= request.POST['txtdireccion']

    guardarcliente=Clientes.objects.create(id_cli=id_cli,nombre=nombre,apellido=apellido, correo=correo, fecha=fecha, telefono=telefono, direccion=direccion)
    return redirect("/")

def seleccionarCliente(request,id_cli):
    cliente = Clientes.objects.get(id_cli=id_cli)
    return render(request,'editarClientes.html',{'misclientes':cliente})

def editarCliente(request):
    id_cli=  request.POST['txtid_cli']
    nombre=  request.POST['txtnombre']
    apellido=  request.POST['txtapellido']
    correo=  request.POST['txtcorreo']
    fecha= request.POST['txtfecha']
    telefono= request.POST['txttelefono']
    direccion= request.POST['txtdireccion']
    cliente = Clientes.objects.get(id_cli=id_cli)
    cliente.nombre=nombre
    cliente.apellido=apellido
    cliente.correo=correo
    cliente.fecha=fecha
    cliente.telefono=telefono
    cliente.direccion=direccion

    cliente.save()
    return redirect("/")

def borrarCliente(request,id_cli):
    cliente=Clientes.objects.get(id_cli=id_cli)
    cliente.delete()
    return redirect("/")
