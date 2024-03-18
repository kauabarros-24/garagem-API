from django.db import models

class Carro(models.Model):
    montadora = models.CharField(max_length=25)
    ano = models.IntegerField(null=False)
    modelo = models.CharField(max_length=20)
    placa = models.CharField(max_length=10, primary_key=1)
    def __str__(self):
        return self.placa
        return self.modelo
        return self.montadora        