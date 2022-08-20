from datetime import datetime
from django.db import models


class Familiar(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.PositiveIntegerField()
    fecha_nacimiento = models.DateField() #año,mes,dia,hora,minuto,segundo...
    
    

   