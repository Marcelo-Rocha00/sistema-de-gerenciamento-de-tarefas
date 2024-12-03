from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
    
    
class FiltroForms(forms.Form):
    STATUS_CHOICES = [
        ('true','Verdadeiro'),
        ('false','Falso')
    ]
    
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True)
    

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='E-mail')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
