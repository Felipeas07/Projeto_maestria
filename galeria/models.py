from django.db import models
from django.contrib.auth.models import User

class Anunciante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome  # Retorna o nome da categoria

class Anuncio(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    fotos = models.ImageField(upload_to='anuncios_fotos/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)  # ID da categoria padrão

    def __str__(self):
        return self.titulo

