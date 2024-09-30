from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm): #criando um formulario personalizado para o modelo padrão User
    #adicionando um campo de e-mail ao fromulario
    email = forms.EmailField(required=True) 
    
    class Meta:
        model = User
        fields = '__all__'
       
    #criando um metodo que salva o usuário. o 'commit' indica que o usuário dever ser salvo no banco de dados 
    def save(self, commit=True):
        
        user = super().save(commit=False)
        
    