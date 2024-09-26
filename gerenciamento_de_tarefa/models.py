from django.db import models
from django.contrib.auth.models import User #criando usuarios utilizando o usuario padrão do django

class task(models.Model):
    Titulo = models.CharField(max_length=100)
    Descrição = models.TextField()
    data_criação = models.DateTimeField()
    Data_limite = models.DateTimeField()
    status = models.BooleanField()
    atribuida_a = models.ForeignKey(User, on_delete=models.CASCADE )
    
    def __str__(self):
        return self.Titulo
