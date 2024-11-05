from django import forms

    
    
class FiltroForms(forms.Form):
    STATUS_CHOICES = [
        ('true','Verdadeiro'),
        ('false','Falso')
    ]
    
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True)