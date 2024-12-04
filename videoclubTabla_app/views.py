from django.shortcuts import render,redirect
from .models import Productos
# Create your views here.
def inicio_vistas(request):
    lasmaterias=Productos.objects.all()
    return render(request,'gestionarMateria.html',{'mismaterias':lasmaterias})

def registrarMateria(request):
    codigo=  request.POST['txtcodigo']
    nombre=  request.POST['txtnombre']
    creditos=  request.POST['numcreditos']
    creditos1=  request.POST['numcreditos1']
    fecha= request.POST['txtfecha']
    descripcion= request.POST['txtdescripcion']
    provedor_id= request.POST['txtprovedor_id']

    guardarmateria=Productos.objects.create(codigo=codigo,nombre=nombre,creditos=creditos, creditos1=creditos1, fecha=fecha, descripcion=descripcion, provedor_id=provedor_id)
    return redirect("productos")

def seleccionarMateria(request,codigo):
    materia = Productos.objects.get(codigo=codigo)
    return render(request,'editarMateria.html',{'mismaterias':materia})

def editarMateria(request):
    codigo=  request.POST['txtcodigo']
    nombre=  request.POST['txtnombre']
    creditos=  request.POST['numcreditos']
    creditos1=  request.POST['numcreditos1']
    fecha= request.POST['txtfecha']
    descripcion= request.POST['txtdescripcion']
    provedor_id= request.POST['txtprovedor_id']
    materia = Productos.objects.get(codigo=codigo)
    materia.nombre=nombre
    materia.creditos=creditos
    materia.creditos1=creditos1
    materia.fecha=fecha
    materia.descripcion=descripcion
    materia.provedor_id=provedor_id

    materia.save()
    return redirect("productos")

def borrarMateria(request,codigo):
    materia=Productos.objects.get(codigo=codigo)
    materia.delete()
    return redirect("productos")
