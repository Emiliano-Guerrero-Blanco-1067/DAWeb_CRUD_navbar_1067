from django.urls import path
from videoclubTabla_app import views
urlpatterns = [
    path('productos',views.inicio_vistas,name='productos'),
    path('registrarMateria/',views.registrarMateria,  name='registrarMateria'),
    path('seleccionarMateria/<codigo>',views.seleccionarMateria,name="seleccionarMateria"),
    path('editarMateria/',views.editarMateria,name="editarMateria"),
    path("borrarMateria/<codigo>",views.borrarMateria,name="borrarMateria")

]