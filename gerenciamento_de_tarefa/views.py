from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib import messages
from .forms import CustomUserCreationForm #importando o formulario personalizado com o e-mail
from .models import Task
from .serializers import taskSerializer
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from .forms import FiltroForms


class taskViewSet(viewsets.ModelViewSet):# criando um viewset para o modelo 'task'
    queryset = Task.objects.all() # Define a queryset como todas as instâncias do modelo 'task'
    serializer_class = taskSerializer # Define o serializer que será usado para converter dados do modelo 'task
    permission_classes = [IsAuthenticated]
    


class SignUp(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'accounts/register.html', {'form': form})
    
    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        print(form)
        
        if form.is_valid():
            form.save()  # Salva o usuário com o email
            messages.success(request, 'Registro realizado com sucesso!')
            return redirect(reverse_lazy('login'))
        else:
            # Adiciona mensagens de erro caso o formulário não seja válido
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

        return render(request, 'accounts/registro.html', {'form': form})
    

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            
            return redirect('usuario')
        else:
            messages.error(request, 'Usuário ou senha incorretos')
            return render(request, 'accounts/login.html')

    return render(request, 'accounts/login.html')
    
def logout_view(request):
    logout(request)
    return redirect('login')
 
    
@login_required
def perfil_usuario(request):
    form = FiltroForms(request.POST or None)
    tasks = Task.objects.filter(usuario=request.user)# Filtra todas as tarefas associadas ao usuário atualmente autenticado.
    status_selecionado = None

    # Captura o termo de busca do campo 'titulo' (enviado por GET)
    titulo_busca = request.GET.get('titulo' '')

    # Filtra as tarefas pelo termo de busca no título, se houver
    if titulo_busca:
        tasks = tasks.filter(titulo__icontains=titulo_busca)
    
    if form.is_valid():
        status_selecionado = form.cleaned_data['status']
        if status_selecionado == 'true':
            tasks = tasks.filter(status=True)  # Filtra tarefas concluídas do usuário
        else:
            tasks = tasks.filter(status=False)  # Filtra tarefas pendentes do usuário

    
    return render(request,'gerenciamento_de_tarefa/pagina_usuario.html' # Especifica o caminho do template HTML a ser usado
     , {'username': request.user.username, 'tasks': tasks, 'form': form, 'status_selecionado': status_selecionado, 'titulo_busca': titulo_busca} )# Envia um dicionário com o nome de usuário logado para o template


@login_required
def add_task(request):# função para adicionar novas tarefas
    if request.method ==  'POST':# Verifica se a requisição é do tipo 'POST', é processa os dados do formulário
        title = request.POST.get('titulo')  # Obtém o título da tarefa
        stats = request.POST.get('status') == 'on'  # Verifica se a checkbox está marcada e define como True ou False
        description = request.POST.get('descricao') # Obtém a descrição da tarefa
        data_limit = request.POST.get('data_limite') # Obtém a data limite da tarefa
        usuario_id = request.POST.get('usuario') # Obtém o ID do usuário associado à tarefa
        if title: # Verifica se o titulo da tarefa não esta vazio
            usuario = User.objects.get(id = usuario_id)## Obtém o objeto do usuário correspondente ao ID fornecido
            Task.objects.create(
            titulo=title,  # Define o título da tarefa
            status=stats,  # Define o status da tarefa (concluída ou pendente)
            usuario=usuario,  # Associa a tarefa ao usuário obtido
            descricao=description,  # Define a descrição da tarefa
            data_limite=data_limit,  # Define a data limite da tarefa
    )
        return redirect('usuario')# Redireciona para pagina de usuario apos a criação da tarefa
    usuarios = User.objects.all() # Obtém todos os usuários do banco 
    # Renderiza o template 'add_task.html', passando a lista de usuários como contexto
    return render(request, 'gerenciamento_de_tarefa/add_task.html', {'usuarios':usuarios })


@login_required
def delete_task(request, task_id): # criando uma Função para deletar uma tarefa específica com base no ID
    task = Task.objects.get(id=task_id) # obtem a tarefa com base no 'ID' fornecido
    task.delete() # Deleta a tarefa encontrada
    return redirect('usuario')# Redireciona para a página do usuário após deletar a tarefa

@login_required
def detalhes_task(request, task_id):
    tasks = get_object_or_404(Task, id= task_id) # Busca a tarefa pelo ID
    return render(request, 'gerenciamento_de_tarefa/detalhes_task.html',{'task':tasks})  # Renderiza o template com a tarefa


@login_required
def editar_tarefa(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    usuarios = User.objects.all()
    
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        status = request.POST.get('status') == 'True'  # Verifica se o checkbox foi marcado
        descricao = request.POST.get('descricao')
        data_limit = request.POST.get('data_limite')
        usuario_id = request.POST.get('usuario')
        
        print(f"Status: {status}")
        
        if titulo and usuario_id:
            usuario = User.objects.get(id = usuario_id)
            task.titulo = titulo
            task.status = status
            task.descricao = descricao
            task.data_limite = data_limit
            task.usuario=usuario
            task.save()
            return redirect('usuario')  # Redireciona após salvar
        
    return render(request, 'gerenciamento_de_tarefa/editar_tasks.html', {'task': task, 'usuarios':usuarios})

def busca_tarefa(request):
    busca = request.GET.get('query', '')
    resultado = Task.objects.filter()
    
    return render(request, 'User/pagina_usuario.html', {'busca': busca})

