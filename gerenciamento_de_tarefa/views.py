from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import task
from .serializers import taskSerializer
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm #importando o formulario personalizado com o e-mail

class taskViewSet(viewsets.ModelViewSet):# criando um viewset para o modelo 'task'
    queryset = task.objects.all() # Define a queryset como todas as instâncias do modelo 'task'
    serializer_class = taskSerializer # Define o serializer que será usado para converter dados do modelo 'task
        
class SignUP(generic.CreateView):#utilizando o 'generic' que ajuda na criação de views
    form_class = CustomUserCreationForm #usando o formulario personalizado
    success_url = reverse_lazy('login') # URL de redirecionamento após registro bem-sucedido
    template_name = 'gerenciamento_de_tarefa/registro.html' #diretorio onde o template se encontra é o nome do arquivo html
        
class Login(LoginView):
    template_name = 'gerenciamento_de_tarefa/login.html'




