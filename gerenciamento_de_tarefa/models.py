from django.db import models
from django.contrib.auth.models import User #criando usuarios utilizando o usuario padrão do django

class task(models.Model): #definindo um modelo pra task
    Titulo = models.CharField(max_length=100) # campo onde o titulo sera inserido, limitado a 100 caracteres
    Descrição = models.TextField()# campo onde é possivel inserir uma descrição detalhada do pedido
    data_criação = models.DateTimeField()# data é hora da criação do pedido
    Data_limite = models.DateTimeField()# data é hora limite para a conclusão da tarefa
    status = models.BooleanField()# Status da tarefa: True se concluida é False caso não esteja concluida ainda
    atribuida_a = models.ForeignKey(User, on_delete=models.CASCADE ) # usuário ao qual a tarefa esta atribuida
    
    def __str__(self):
        return self.Titulo #retornando o título da tarefa como representação da instância
