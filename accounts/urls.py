from django.urls import path
from .views import SignUp, login_view, logout_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', SignUp.as_view(), name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

     #URL de formulario para redefinir a senha
    path('login/redefinir/', auth_views.PasswordResetView.as_view(template_name ='Register/password_reset_form.html'), name='senha_redifinir'),

    #URL que sera exibido quando o e-mail de recuperação for enviado
    path('login/redefinir/enviado/', auth_views.PasswordResetDoneView.as_view(template_name = 'Register/password_reset_done.html'), name="password_reset_done"),

    #URL que confirma a redifinição da senha(após o usuário clicar no link do e-mail)
    path('login/redefinir/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='Register/password_reset_confirm.html'), name='password_reset_confirm'),

    #URL que será exibido após a conclusão da redifinição da senha
    path('login/redefinir/concluido/', auth_views.PasswordResetCompleteView.as_view(template_name='Register/password_reset_complete.html'), name='password_reset_complete'),
    
]
