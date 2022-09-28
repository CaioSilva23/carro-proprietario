from django.shortcuts import render
from .models import *


# Create your views here.

def carro_detalhe(request, id):
    motoristas = Motorista.objects.get(id=id)

    carros = Carro.objects.filter(motorista_id=motoristas.id)

    context = {

        "carros": carros,

        "motoristas": motoristas,

    }

    return render(request, "carro_detalhe.html", context)
