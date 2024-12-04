from django.urls import path
from sucursal_app import views
urlpatterns = [
    path('sucursales',views.inicio_vistaSucursales,name='sucursales'),
    path('registrarSucursales/',views.registrarSucursales,  name='registrarSucursales'),
    path('seleccionarSucursales/<id>',views.seleccionarSucursales,name="seleccionarSucursales"),
    path('editarSucursales/',views.editarSucursales,name="editarSucursales"),
    path("borrarSucursales/<id>",views.borrarSucursales,name="borrarSucursales")

]