from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Categoria
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    avatar = forms.ImageField(required=False)  # Novo campo para upload de avatar

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "avatar")  # Inclui avatar nos campos

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        
        # Adiciona o avatar ao usuário se fornecido
        if self.cleaned_data.get('avatar'):
            user.avatar = self.cleaned_data['avatar']
        
        if commit:
            user.save()
        return user

class AnuncioFilterForm(forms.Form):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), required=False)
    valor_min = forms.DecimalField(required=False, min_value=0, label="Valor mínimo")
    valor_max = forms.DecimalField(required=False, min_value=0, label="Valor máximo")

class ContactForm(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensagem = forms.CharField(widget=forms.Textarea)