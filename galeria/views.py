from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponse
from .forms import CustomUserCreationForm

def index(request):
    return render(request, 'galeria/index.html')

def servicos(request):
    return render(request, 'galeria/servicos.html')

def sobre(request):
    return render(request, 'galeria/sobre.html')

def cadastro(request):
    return render(request, 'galeria/cadastro.html')

def contato(request):
    return render(request, 'galeria/contato.html')

def user_login(request):  # Renomeie esta função para evitar conflito
    return render(request, 'galeria/login.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user.is_superuser:
            return redirect('/admin/')  # Redireciona para a página de admin
        elif user is not None:
            auth_login(request, user)  # Renomeie a função de login para evitar conflito com a view
            return redirect('index')  # Redireciona para a página 'index' após login
        else:
            return render(request, 'galeria/login.html', {'error': 'Usuário ou senha inválidos'})
    else:
        return render(request, 'galeria/login.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:  # Verifica se o usuário foi autenticado
                auth_login(request, user)  # Chamada correta para a função login do Django
                return redirect('index')  # Redireciona para a página inicial após login automático
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'galeria/register.html', {'form': form})

# Função de logout
def logout_view(request):
    if request.method == 'POST' or request.method == 'GET':
        auth_logout(request)
        return render(request, 'galeria/logout.html')  # Redireciona para a página de logout
    else:
        return redirect('index')  # Redireciona para a página inicial se o método não for suportado
