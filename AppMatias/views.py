from http.client import HTTPResponse
from mailbox import NoSuchMailboxError
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from AppMatias.models import Familiar


def familiar(request):
    
    familiar1 = Familiar(nombre="Claudia", apellido="Roger", edad=58, fecha_nacimiento="1964-7-17")
    familiar1.save()
    contexto = {
        "familiar":familiar1,
            }
    return render(request, 'AppMatias/familiares.html', contexto)


def familiar2(request):
    
    contexto={
        'nombre':'Julio', 
        'apellido':'Zucchi',
        'edad': 59,
        'fecha_nacimiento': '1963-4-15',
    }
    
    return render(request, 'AppMatias/familiares2.html', contexto)


def familiar3(request):
    
    contexto={
        'nombre':'Bautista', 
        'apellido':'Zucchi',
        'edad': 16,
        'fecha_nacimiento': '2005-9-20',
    }
    
    return render(request, 'AppMatias/familiares3.html', contexto)


def inicio(request):
    
    return render(request, 'index.html')