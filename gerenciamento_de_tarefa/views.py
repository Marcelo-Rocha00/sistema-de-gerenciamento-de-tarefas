from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Task
from .serializers import taskSerializer
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm #importando o formulario personalizado com o e-mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


class taskViewSet(viewsets.ModelViewSet):# criando um viewset para o modelo 'task'
    queryset = Task.objects.all() # Define a queryset como todas as instâncias do modelo 'task'
    serializer_class = taskSerializer # Define o serializer que será usado para converter dados do modelo 'task
        
class SignUP(generic.CreateView):#utilizando o 'generic' que ajuda na criação de views
    form_class = CustomUserCreationForm #usando o formulario personalizado
    success_url = reverse_lazy('login') # URL de redirecionamento após registro bem-sucedido
    template_name = 'User/registro.html' #diretorio onde o template se encontra é o nome do arquivo html
        
#casse personalizada para o processo de login
class Login(LoginView):#essa classe herda 'LoginView' padrão do jogo, que ja tem toda a logica de autenticação de usuários
    template_name = 'User/login.html'#formulario HTML para a personalização da pagina

@login_required#decoretor que para o usuario acessar a pagina de usuario é necessario estar logado
def perfil_usuario(request):
    tasks = Task.objects.all().filter(usuario=request.user)
    return render(request,'User/pagina_usuario.html' # Especifica o caminho do template HTML a ser usado
     , {'username': request.user.username, 'tasks': tasks} )# Envia um dicionário com o nome de usuário logado para o template

@login_required
def add_task(request):
    if request.method ==  'POST':
        title = request.POST.get('titulo')
        stats = request.POST.get('status') == 'on'
        usuario_id = request.POST.get('usuario')
        if title:
            usuario = User.objects.get(id = usuario_id)
            Task.objects.create(titulo=title, status=stats, usuario = usuario,)
        return redirect('usuario')
    usuarios = User.objects.all()
    return render(request, 'User/add_task.html', {'usuarios':usuarios })


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('usuario')