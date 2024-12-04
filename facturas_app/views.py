from django.shortcuts import render,redirect
from .models import Facturas
# Create your views here.
def inicio_vistaFacturas(request):
    lasmaterias=Facturas.objects.all()
    return render(request,'gestionarFacturas.html',{'mismaterias':lasmaterias})

def registrarFacturas(request):
    id_fac=  request.POST['txtid_fac']
    total=  request.POST['txttotal']
    area=  request.POST['txtarea']
    estado=  request.POST['txtestado']
    fecha= request.POST['txtfecha']
    met_pago= request.POST['txtmet_pago']
    id_suc= request.POST['txtid_suc']
    id_prod=request.POST['txtid_prod']
    id_cli=request.POST['txtid_cli']
    id_emp=request.POST['txtid_emp']

    guardarmateria=Facturas.objects.create(id_fac=id_fac,total=total,area=area, estado=estado, fecha=fecha, met_pago=met_pago, id_suc=id_suc, id_prod=id_prod, id_cli=id_cli, id_emp=id_emp, )
    return redirect("/")

def seleccionarFacturas(request,id_fac):
    materia = Facturas.objects.get(id_fac=id_fac)
    return render(request,'editarFacturas.html',{'mismaterias':materia})

def editarFacturas(request):
    id_fac=  request.POST['txtid_fac']
    total=  request.POST['txttotal']
    area=  request.POST['txtarea']
    estado=  request.POST['txtestado']
    fecha= request.POST['txtfecha']
    met_pago= request.POST['txtmet_pago']
    id_suc= request.POST['txtid_suc']
    id_prod= request.POST['txtid_prod']
    id_cli= request.POST['txtid_cli']
    id_emp= request.POST['txtid_emp']
    materia = Facturas.objects.get(id_fac=id_fac)
    materia.total=total
    materia.area=area
    materia.estado=estado
    materia.fecha=fecha
    materia.met_pago=met_pago
    materia.id_suc=id_suc
    materia.id_prod=id_prod
    materia.id_cli=id_cli
    materia.id_emp=id_emp

    materia.save()
    return redirect("/")

def borrarFacturas(request,id_fac):
    materia=Facturas.objects.get(id_fac=id_fac)
    materia.delete()
    return redirect("/")
