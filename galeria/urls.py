from django.urls import path
from galeria.views import index, servicos, sobre, cadastro, contato
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('anuncios/', views.lista_anuncios, name='lista_anuncios'),
    path('buscar/', views.buscar_anuncios, name='buscar_anuncios'),
    path('contato/', views.contato, name='contato'),
    path('servicos/', views.servicos, name='servicos'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

