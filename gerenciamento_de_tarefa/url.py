from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth.views import LogoutView
from .views import taskViewSet
from . import views

router = DefaultRouter() # Cria uma instância do roteador padrão
router.register(r'task', taskViewSet) # Registra o viewset de tarefas na rota 'task'

urlpatterns = [
    path('api/', include(router.urls)), #uma rota url para acesso da API
    path('registro/', views.SignUP.as_view(), name='registro'),  #Rota de acesso a pagina de registro
    path('login/', views.Login.as_view(), name = 'login'),
    path('usuario/', views.perfil_usuario, name = 'usuario' ),
    path('logout/',LogoutView.as_view(next_page='login'), name= 'logout'),
   
] 




