from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import taskViewSet
from . import views



router = DefaultRouter() # Cria uma instância do roteador padrão
router.register(r'task', taskViewSet) # Registra o viewset de tarefas na rota 'task'

urlpatterns = [
     #uma rota url para acesso da API
    path('api/', include(router.urls)),

    #URL para a pagina de usuario
    path('usuario/', views.perfil_usuario, name = 'usuario' ),

    #URL de adição de tarefas
    path('add/', views.add_task, name='add_task'),

    #Url para deletar as tarefas
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),

    #Url de uma pagina que exibe os detalhes das tarefas
    path('task/<int:task_id>', views.detalhes_task, name='detalhes_task'),

    #URL para edição de tarefas
    path('edit/<int:task_id>/',views.editar_tarefa, name='editar_task')
] 




