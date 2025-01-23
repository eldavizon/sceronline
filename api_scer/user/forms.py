from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
                        
        fields = ['username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        self.fields['username'].label = "Nome de Usuário"
        self.fields['email'].label = "Endereço de E-mail"
        self.fields['password1'].label = "Senha"
        self.fields['password2'].label = "Confirmação de Senha"