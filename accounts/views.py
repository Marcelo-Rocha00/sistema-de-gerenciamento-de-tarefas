from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.views import View
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm




class SignUp(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'accounts/register.html', {'form': form})
    
    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        print(form)
        
        if form.is_valid():
            form.save()  # Salva o usuário com o email
            messages.success(request, 'Registro realizado com sucesso!')
            return redirect(reverse_lazy('login'))
        else:
            # Adiciona mensagens de erro caso o formulário não seja válido
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

        return render(request, 'accounts/register.html', {'form': form})




def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou senha incorretos')
            return render(request, 'accounts/login.html')

    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


