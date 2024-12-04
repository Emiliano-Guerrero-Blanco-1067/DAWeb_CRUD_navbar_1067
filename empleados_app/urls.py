from django.urls import path
from empleados_app import views
urlpatterns = [
    path('empleados',views.inicio_vistaEmpleados,name='empleados'),
    path('registrarEmpleado/',views.registrarEmpleado,  name='registrarEmpleado'),
    path('seleccionarEmpleado/<id_emp>',views.seleccionarEmpleado,name="seleccionarEmpleado"),
    path('editarEmpleado/',views.editarEmpleado,name="editarEmpleado"),
    path("borrarEmpleado/<id_emp>",views.borrarEmpleado,name="borrarEmpleado")

]