from django.urls import path
from AppMatias.views import familiar, familiar2, familiar3, inicio


urlpatterns = [

    path('familiar/', familiar, name='AppMatiasFamiliar'),
    path('familiar2/', familiar2, name='AppMatiasFamiliar2'),
    path('familiar3/', familiar3, name='AppMatiasFamiliar3'),
    path('', inicio, name='AppMatiasInicio'),
    
]
