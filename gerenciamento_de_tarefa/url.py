from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth.views import LogoutView
from .views import taskViewSet
from . import views
from django.contrib.auth import views as auth_views

router = DefaultRouter() # Cria uma instância do roteador padrão
router.register(r'task', taskViewSet) # Registra o viewset de tarefas na rota 'task'

urlpatterns = [
     #uma rota url para acesso da API
    path('api/', include(router.urls)),

    #URL de acesso a pagina de registro
    path('registro/', views.SignUP.as_view(), name='registro'), 

    #URL de acesso a pagina de login
    path('login/', views.Login.as_view(), name = 'login'), 

    #URL para a pagina de usuario
    path('usuario/', views.perfil_usuario, name = 'usuario' ),

    #URL para a pagina de logout, apos acessar a pagina logout o usuario sera redirecionado para a pagina login
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    #URL de formulario para redefinir a senha
    path('login/redefinir/', auth_views.PasswordResetView.as_view(template_name ='gerenciamento_de_tarefa/password_reset_form.html'), name='senha_redifinir'),

    #URL que sera exibido quando o e-mail de recuperação for enviado
    path('login/redefinir/enviado/', auth_views.PasswordResetDoneView.as_view(template_name = 'gerenciamento_de_tarefa/password_reset_done.html'), name="password_reset_done"),

    #URL que confirma a redifinição da senha(após o usuário clicar no link do e-mail)
    path('login/redefinir/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='gerenciamento_de_tarefa/password_reset_confirm.html'), name='password_reset_confirm'),

    #URL que será exibido após a conclusão da redifinição da senha
    path('login/redefinir/concluido/', auth_views.PasswordResetCompleteView.as_view(template_name='gerenciamento_de_tarefa/password_reset_complete.html'), name='password_reset_complete'),
] 




