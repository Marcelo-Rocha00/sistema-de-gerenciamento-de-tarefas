from django.urls import path
from .views import SignUp, login_view, logout_view
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
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
    
    
]
