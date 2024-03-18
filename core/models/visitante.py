from django.db import models

class Visitante(models.Model):
    nome = models.CharField(max_length=100)
    entrada = models.IntegerField(unique=True)
    email = models.EmailField(unique=True, null=True)
    def __str__(self):
        return self.nome
        