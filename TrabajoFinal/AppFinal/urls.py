from django.urls import path
from AppFinal import views
from .views import *

urlpatterns = [
    path('/', views.inicio, name="inicio"),
    
    #path('creaCurso', curso),
    
    path('/empleado', views.empleado, name="Empleado"),
    path('/conductor', views.conductor, name="Conductor"),
    path('/camion', views.camion, name="Camion"),
    path('/empleadosadd', views.empleadosadd, name= 'agregarEmpleado'),
    path('/conductoresadd', views.conductoresadd, name= 'agregarConductor'),
    path('/camionesadd', views.camionesadd, name= 'agregarCamion'),
    path('/empleadosdel/<id>', empleadosdel, name= 'empleadosdel'),
    path('/conductoresdel/<id>', conductoresdel, name= 'conductoresdel'),
    path('/camionesdel/<id>', camionesdel, name= 'camionesdel'),
    path('/empleadosSearch', empleadosSearch, name= 'empleadosSearch'),
    path('/conductoresSearch',conductoresSearch , name= 'conductoresSearch'),
    path('/camionesSearch/', camionesSearch, name= 'camionesSearch'),
    path('/camionesResults/', buscarCamion, name= 'buscarCamion'),

]