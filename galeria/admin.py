from django.contrib import admin
from django import forms
from .models import Anuncio, Profile

# Registro do modelo Anuncio no admin
admin.site.register(Anuncio)

# Formulário personalizado para Profile
class ProfileAdminForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'  # Ou liste os campos específicos

# Classe personalizada de admin para Profile
class ProfileAdmin(admin.ModelAdmin):
    form = ProfileAdminForm
    list_display = ('user', 'avatar')  # Adicione campos que deseja exibir na lista do admin

# Registro do modelo Profile no admin com personalização
admin.site.register(Profile, ProfileAdmin)
