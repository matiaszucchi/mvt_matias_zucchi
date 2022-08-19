from http.client import HTTPResponse
from mailbox import NoSuchMailboxError
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from AppMatias.models import Familiar


def familiar(request):
    
    familiar1 = Familiar(nombre="Claudia", apellido="Roger", edad=58)
    familiar1.save()
    contexto = {
        "familiar":familiar1,
            }
    return render(request, 'familiares.html', contexto)


def familiardos(request):
    
    familiar2 = Familiar(nombre="Julio", apellido="Zucchi", edad=59)
    familiar2.save()
    contexto = {
        "familiardos":familiar2,
            }
    return render(request, 'familiares.html', contexto)


def familiartres(request):
    
    familiar3 = Familiar(nombre="Bautista", apellido="Zucchi", edad=16)
    familiar3.save()
    contexto = {
        "familiar":familiar3,
            }
    return render(request, 'familiares.html', contexto)

