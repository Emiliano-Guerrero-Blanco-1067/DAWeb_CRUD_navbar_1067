from django.shortcuts import render,redirect
from .models import Empleados
# Create your views here.
def inicio_vistaEmpleados(request):
    lasmaterias=Empleados.objects.all()
    return render(request,'gestionarEmpleados.html',{'mismaterias':lasmaterias})

def registrarEmpleado(request):
    id_emp=  request.POST['txtid_emp']
    nombre=  request.POST['txtnombre']
    apellido=  request.POST['txtapellido']
    puesto=  request.POST['txtpuesto']
    fecha_contratacion= request.POST['txtfecha_contratacion']
    salario_quincena= request.POST['txtsalario_quincena']
    dni= request.POST['txtdni']
    id_suc= request.POST['txtid_suc']

    guardarEmpleado=Empleados.objects.create(id_emp=id_emp,nombre=nombre,apellido=apellido, puesto=puesto, fecha_contratacion=fecha_contratacion, salario_quincena=salario_quincena, dni=dni, id_suc=id_suc)
    return redirect("/")

def seleccionarEmpleado(request,id_emp):
    materia = Empleados.objects.get(id_emp=id_emp)
    return render(request,'editarEmpleados.html',{'mismaterias':materia})

def editarEmpleado(request):
    id_emp=  request.POST['txtid_emp']
    nombre=  request.POST['txtnombre']
    apellido=  request.POST['txtapellido']
    puesto=  request.POST['txtpuesto']
    fecha_contratacion= request.POST['txtfecha_contratacion']
    salario_quincena= request.POST['txtsalario_quincena']
    dni= request.POST['txtdni']
    id_suc= request.POST['txtid_suc']
    materia = Empleados.objects.get(id_emp=id_emp)
    materia.nombre=nombre
    materia.apellido=apellido
    materia.puesto=puesto
    materia.fecha_contratacion=fecha_contratacion
    materia.salario_quincena=salario_quincena
    materia.dni=dni
    materia.id_suc=id_suc

    materia.save()
    return redirect("/")

def borrarEmpleado(request,id_emp):
    materia=Empleados.objects.get(id_emp=id_emp)
    materia.delete()
    return redirect("/")
