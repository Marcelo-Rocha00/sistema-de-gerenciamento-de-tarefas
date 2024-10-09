from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm): #criando um formulario personalizado para o modelo padrão User
    #adicionando um campo de e-mail ao fromulario
    email = forms.EmailField(required=True) #definindo que o email é obrigatorio
    
    class Meta:
        model = User #utilizando o modelo usuario
        fields = ['username', 'email', 'password1', 'password2']#incluindo todos os campos desejados
       
    #criando um metodo que salva o usuário. o 'commit' indica que o usuário dever ser salvo no banco de dados 
    def save(self, commit=True): 
        
        #O método 'super()' chama o método 'save' da classe pai (UserCreationForm)
        #O 'commit=False' é utilizado para evitar que o usuário seja salvo no banco de dados imediatamente.
        #permitindo que eu faça modificações nos dados do usuário(que nesse codigo é atribuir o e-mail) antes de salvar
        user = super().save(commit=False) 
        
        #atribuindo o e-mail fornecido pelo formulário ao campo 'e-mail' do usuário.
        user.email = self.cleaned_data['email'] #'cleaned_data' contém os dados validados do formulário
        
        if commit:
            user.save()#finalmente salvando o usuario no banco de dados
        
        # Retornamos a instância do usuário, que pode ser utilizada após o salvamento
        return user
    