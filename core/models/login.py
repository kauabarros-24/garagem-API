#Login no site da garagem
from django.db import models

class Login(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=False)
    telefone = models.IntegerField(null=True)
    def __str__(self):
        return self.nome