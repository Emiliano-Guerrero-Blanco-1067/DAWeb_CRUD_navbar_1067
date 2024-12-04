from django.urls import path
from provedores_app import views
urlpatterns = [
    path('provedores',views.inicio_vistaProvedores,name='provedores'),
    path('registrarProvedores/',views.registrarProvedores,  name='registrarProvedores'),
    path('seleccionarProvedores/<id_prov>',views.seleccionarProvedores,name="seleccionarProvedores"),
    path('editarProvedores/',views.editarProvedores,name="editarProvedores"),
    path("borrarProvedores/<id_prov>",views.borrarProvedores,name="borrarProvedores")

]