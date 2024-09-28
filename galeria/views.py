from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import CustomUserCreationForm
from .models import Anuncio
from .forms import AnuncioFilterForm, ContactForm
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    return render(request, 'galeria/index.html')

def servicos(request):
    anuncios = Anuncio.objects.all()  # Busca todos os anúncios do banco de dados
    return render(request, 'galeria/servicos.html', {'anuncios': anuncios})

def buscar_anuncios(request):
    form = AnuncioFilterForm(request.GET or None)
    anuncios = Anuncio.objects.all()
    if form.is_valid():
        if form.cleaned_data.get('categoria'):
            anuncios = anuncios.filter(categoria=form.cleaned_data['categoria'])
        if form.cleaned_data.get('valor_min'):
            anuncios = anuncios.filter(valor__gte=form.cleaned_data['valor_min'])
        if form.cleaned_data.get('valor_max'):
            anuncios = anuncios.filter(valor__lte=form.cleaned_data['valor_max'])
    return render(request, 'galeria/servicos.html', {'form': form, 'anuncios': anuncios})


def lista_anuncios(request):
    anuncios = Anuncio.objects.all()
    return render(request, 'galeria/servicos.html', {'anuncios': anuncios})


def sobre(request):
    return render(request, 'galeria/sobre.html')

def cadastro(request):
    return render(request, 'galeria/cadastro.html')

def contato(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        motivo = request.POST.get('motivo')
        mensagem = request.POST.get('mensagem')
        
        # Envio do e-mail
        send_mail(
            f"Contato: {motivo}",
            f"Mensagem de {email}:\n\n{mensagem}",
            settings.DEFAULT_FROM_EMAIL,  # Endereço de origem configurado no settings
            ['felipeas.inf@gmail.com'],  # Substitua pelo e-mail do destinatário
        )
        return render(request, 'galeria/contato.html', {'success': True})

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
        form = CustomUserCreationForm(request.POST, request.FILES)  # Inclui request.FILES para lidar com o upload de arquivos
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:  # Verifica se o usuário foi autenticado
                auth_login(request, user)  # Faz login automático após o cadastro
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
    



