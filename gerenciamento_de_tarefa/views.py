from rest_framework import viewsets
from .models import task
from .serializers import taskSerializer
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm #importando o formulario personalizado com o e-mail

class taskViewSet(viewsets.ModelViewSet):
    queryset = task.objects.all()
    serializer_class = taskSerializer
        
class SignUP(generic.CreateView):#utilizando o 'generic' que ajuda na criação de views
    form_class = CustomUserCreationForm #usando o formulario personalizado
    success_url = reverse_lazy('login') # URL de redirecionamento após registro bem-sucedido
    template_name = 'gerenciamento_de_tarefa/registro.html' ## Nome do template HTML a ser renderizado para o registro
        
        


