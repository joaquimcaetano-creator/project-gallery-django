from django.contrib import admin
from .models import Projeto, Evento

# Registro do Modelo de Projetos
@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'area', 'data_cadastro')
    search_fields = ('titulo', 'autor')
    list_filter = ('area',)

# Registro do Modelo de Eventos
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'categoria')
    list_filter = ('categoria', 'data_evento')
    search_fields = ('titulo',)