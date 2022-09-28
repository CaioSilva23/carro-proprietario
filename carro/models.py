from django.db import models


# Create your models here.
class Motorista(models.Model):
    nome = models.TextField()
    licenca = models.TextField()


class Carro(models.Model):
    make = models.TextField()

    model = models.TextField()

    year = models.IntegerField()

    vin = models.TextField()

    motorista = models.ForeignKey("Motorista", on_delete=models.SET_NULL, null=True)
