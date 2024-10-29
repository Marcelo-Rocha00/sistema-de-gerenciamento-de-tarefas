from django.shortcuts import render, redirect, get_object_or_404
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
    tasks = Task.objects.filter(usuario=request.user)# Filtra todas as tarefas associadas ao usuário atualmente autenticado.
    return render(request,'User/pagina_usuario.html' # Especifica o caminho do template HTML a ser usado
     , {'username': request.user.username, 'tasks': tasks} )# Envia um dicionário com o nome de usuário logado para o template

@login_required
def add_task(request):# função para adicionar novas tarefas
    if request.method ==  'POST':# Verifica se a requisição é do tipo 'POST', é processa os dados do formulário
        title = request.POST.get('titulo')  # Obtém o título da tarefa
        stats = request.POST.get('status') == 'on'  # Verifica se a checkbox está marcada e define como True ou False
        description = request.POST.get('descricao') # Obtém a descrição da tarefa
        data_create = request.POST.get('data_criacao') #Obtém a data de criação da tarefa
        data_limit = request.POST.get('data_limite') # Obtém a data limite da tarefa
        usuario_id = request.POST.get('usuario') # Obtém o ID do usuário associado à tarefa
        if title: # Verifica se o titulo da tarefa não esta vazio
            usuario = User.objects.get(id = usuario_id)## Obtém o objeto do usuário correspondente ao ID fornecido
            Task.objects.create(
            titulo=title,  # Define o título da tarefa
            status=stats,  # Define o status da tarefa (concluída ou pendente)
            usuario=usuario,  # Associa a tarefa ao usuário obtido
            descricao=description,  # Define a descrição da tarefa
            data_criacao=data_create,  # Define a data de criação da tarefa
            data_limite=data_limit,  # Define a data limite da tarefa
    )
        return redirect('usuario')# Redireciona para pagina de usuario apos a criação da tarefa
    usuarios = User.objects.all() # Obtém todos os usuários do banco 
    # Renderiza o template 'add_task.html', passando a lista de usuários como contexto
    return render(request, 'User/add_task.html', {'usuarios':usuarios })


def delete_task(request, task_id): # criando uma Função para deletar uma tarefa específica com base no ID
    task = Task.objects.get(id=task_id) # obtem a tarefa com base no 'ID' fornecido
    task.delete() # Deleta a tarefa encontrada
    return redirect('usuario')# Redireciona para a página do usuário após deletar a tarefa


def detalhes_task(request, task_id):
    tasks = get_object_or_404(Task, id= task_id) # Busca a tarefa pelo ID
    return render(request, 'User/detalhes_task.html',{'task':tasks})  # Renderiza o template com a tarefa

@login_required
def editar_tarefa(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        status = 'status' in request.POST  # Verifica se o checkbox foi marcado
        descricao = request.POST.get('descricao')
        data_create = request.POST.get('data_criacao')
        data_limit = request.POST.get('data_limite')
        usuario_id = request.POST.get('usuario')
        
        if titulo:
            usuario = User.objects.get(id = usuario_id)
            task.titulo = titulo
            task.status = status
            task.descricao = descricao
            task.data_criacao = data_create
            task.data_limite = data_limit
            usuario=usuario
            task.save()
            return redirect('usuario')  # Redireciona após salvar
        
    return render(request, 'User/editar_tasks.html', {'task': task})
