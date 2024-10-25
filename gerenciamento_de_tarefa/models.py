from django.db import models
from django.contrib.auth.models import User #criando usuarios utilizando o usuario padrão do django

class Task(models.Model): #definindo um modelo pra task
    titulo = models.CharField(max_length=100, blank=True) # campo onde o titulo sera inserido, limitado a 100 caracteres
    descrição = models.TextField( blank=True)# campo onde é possivel inserir uma descrição detalhada do pedido
    data_criação = models.DateTimeField(auto_now_add=True, blank=True)# data é hora da criação do pedido
    data_limite = models.DateTimeField( blank=True,null=True)# data é hora limite para a conclusão da tarefa
    status = models.BooleanField(default=False, blank=True)# Status da tarefa: True se concluida é False caso não esteja concluida ainda
    atribuida_a = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,null=True ) # usuário ao qual a tarefa esta atribuida
    
    def __str__(self):
        return self.titulo #retornando o título da tarefa como representação da instância
