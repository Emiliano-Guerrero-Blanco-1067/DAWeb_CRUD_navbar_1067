from django.urls import path
from facturas_app import views
urlpatterns = [
    path('facturas',views.inicio_vistaFacturas,name='facturas'),
    path('registrarFacturas/',views.registrarFacturas,  name='registrarFacturas'),
    path('seleccionarFacturas/<id_fac>',views.seleccionarFacturas,name="seleccionarFacturas"),
    path('editarFacturas/',views.editarFacturas,name="editarFacturas"),
    path("borrarFacturas/<id_fac>",views.borrarFacturas,name="borrarFacturas")

]