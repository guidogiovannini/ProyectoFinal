from django import http
#from .forms import *
from django.template import Template, Context, loader
from django.shortcuts import render, redirect
from .models import Empleado, Conductor, Camion
from django.http import HttpResponse

# Create your views here.
#def empleado(request):
    #return render(request, 'empleadosTemp.html')

#def conductor(request):
    #return render(request, 'conductorTemp.html')

#def camion(request):
    #return render(request, 'camionesTemp.html')

def inicio(request):
    return render(request, 'Inicio.html')

# Mostrar listas

def empleado(request):
    #plantilla=loader.get_template("template1.html")
    listaemp = Empleado.objects.all()
    Context = {'listaemp':listaemp}
    #contexto = Context(listaemp)
    #documento=plantilla.render()
    return render(request, "empleadosTemp.html", Context)

def camion(request):
    #plantilla=loader.get_template("template1.html")
    listacam = Camion.objects.all()
    Context = {'listacam':listacam}
    ##contexto = Context(listacam)
    #documento=plantilla.render()
    return render(request, "camionesTemp.html", Context)

def conductor(request):
    #plantilla=loader.get_template("template1.html")
    listacon = Conductor.objects.all()
    Context = {'listacon':listacon}
    #contexto = Context(listafam)
    #documento=plantilla.render()
    return render(request, "conductorTemp.html", Context)

def empleadosadd(request):
    Documento = request.POST["Documento"]
    Nombre = request.POST["Nombre"]
    Apellido = request.POST["Apellido"]
    Telefono = request.POST["Telefono"]
    Contacto = request.POST["Contacto"]
    addemp = Empleado(Documento=Documento, Nombre=Nombre, Apellido=Apellido, Telefono=Telefono, Contacto=Contacto)
    addemp.save()
    return redirect('/AppFinal/empleado')

def conductoresadd(request):
    Documento = request.POST["Documento"]
    Nombre = request.POST["Nombre"]
    Apellido = request.POST["Apellido"]
    Telefono = request.POST["Telefono"]
    Contacto = request.POST["Contacto"]
    addcon = Conductor(Documento=Documento, Nombre=Nombre, Apellido=Apellido, Telefono=Telefono, Contacto=Contacto)
    addcon.save()
    return redirect('/AppFinal/conductor')

def camionesadd(request):
    Patente = request.POST["Patente"]
    Marca = request.POST["Marca"]
    Color = request.POST["Color"]
    TipoCarga = request.POST["TipoCarga"]
    addcam = Camion(Patente=Patente, Marca=Marca, Color=Color, TipoCarga=TipoCarga)
    addcam.save()
    return redirect('/AppFinal/camion')

def empleadosdel(request, id):
    borrar_emp = Empleado.objects.get(id=id)
    borrar_emp.delete()
    return redirect('/AppFinal/empleado')

def conductoresdel(request, id):
    borrar_con = Conductor.objects.get(id=id)
    borrar_con.delete()
    return redirect('/AppFinal/conductor')

def camionesdel(request, id):
    borrar_cam = Camion.objects.get(id=id)
    borrar_cam.delete()
    return redirect('/AppFinal/camion')

def empleadosSearch(request):
    return render(request, 'empleadosSearch.html')
def conductoresSearch(request):
    return render(request,'conductoresSearch.html')
def camionesSearch(request):
    return render(request, 'camionesSearch.html')

def buscarCamion(request):
    if request.GET['Patente']:
        patente = request.GET['Patente']
        camiones = Camion.objects.filter(Patente=patente)
        return render(request, 'camionesResults.html', {'camiones':camiones, 'patente':patente})
    else:
        respuesta="No se ingreso ningun camión"
        return render(request, 'camionesResults.html', {'respuesta':respuesta})

    return render(request, 'camion.html')