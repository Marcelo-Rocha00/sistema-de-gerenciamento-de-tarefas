from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from .views import taskViewSet, SignUp, logout_view , login_view
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter() # Cria uma instância do roteador padrão
router.register(r'task', taskViewSet) # Registra o viewset de tarefas na rota 'task'

urlpatterns = [
    
    path('detalhes_user/<int:User_id>/', views.detalhes_user, name= 'detalhes_user'),

    path('lista_user/', views.lista_user, name='lista_user' ),

    #rota de registro
    path('register/', SignUp.as_view(), name='registro'),
    
    #rota de Login
    path('', login_view, name='login'),
    
    #rota de logout
    path('logout/', logout_view, name='logout'),

    #URL para a pagina de usuario
    path('usuario/', views.perfil_usuario, name = 'usuario' ),

    #URL de adição de tarefas
    path('add/', views.add_task, name='add_task'),

    #Url para deletar as tarefas
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),

    #Url de uma pagina que exibe os detalhes das tarefas
    path('task/<int:task_id>', views.detalhes_task, name='detalhes_task'),

    #URL para edição de tarefas
    path('edit/<int:task_id>/',views.editar_tarefa, name='editar_task'),

     #URL de formulario para redefinir a senha
    path('login/redefinir/', auth_views.PasswordResetView.as_view(template_name ='accounts/password_reset_form.html'), name='senha_redifinir'),

    #URL que sera exibido quando o e-mail de recuperação for enviado
    path('login/redefinir/enviado/', auth_views.PasswordResetDoneView.as_view(template_name = 'accounts/password_reset_done.html'), name="password_reset_done"),

    #URL que confirma a redifinição da senha(após o usuário clicar no link do e-mail)
    path('login/redefinir/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),

    #URL que será exibido após a conclusão da redifinição da senha
    path('login/redefinir/concluido/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
    
    #endepoints para obter e reiniciar o token jwt
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
     
    #uma rota url para acesso da API
    path('api/', include(router.urls)),
] 




