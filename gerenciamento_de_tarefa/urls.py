from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SignUp, login_view, logout_view
from django.contrib.auth import views as auth_views
from .views import taskViewSet
from . import views

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

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
    path('edit/<int:task_id>/',views.editar_tarefa, name='editar_task'),
    
    
    path('register/', SignUp.as_view(), name='signup'),
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

     #URL de formulario para redefinir a senha
    path('login/redefinir/', auth_views.PasswordResetView.as_view(template_name ='registration/password_reset_form.html'), name='senha_redifinir'),

    #URL que sera exibido quando o e-mail de recuperação for enviado
    path('login/redefinir/enviado/', auth_views.PasswordResetDoneView.as_view(template_name = 'registration/password_reset_done.html'), name="password_reset_enviada"),

    #URL que confirma a redifinição da senha(após o usuário clicar no link do e-mail)
    path('login/redefinir/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirmada'),

    #URL que será exibido após a conclusão da redifinição da senha
    path('login/redefinir/concluido/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_completa'),
    
    

    
    #endepoints para obter e reiniciar o token jwt
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] 




