from django.contrib import admin
from .models import Projeto, Evento, LinhaPesquisa

# --- Registro do Modelo de Projetos ---
@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'area', 'data_cadastro')
    search_fields = ('titulo', 'autor')
    list_filter = ('area',)

# --- Registro do Modelo de Eventos ---
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'categoria')
    list_filter = ('categoria', 'data_evento')
    search_fields = ('titulo',)

# --- Registro do Modelo de Linhas de Pesquisa ---
@admin.register(LinhaPesquisa)
class LinhaPesquisaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'cor_card')
    search_fields = ('titulo', 'descricao')

# NOTA: Não precisamos de admin.site.register(Projeto) aqui embaixo 
# porque o @admin.register lá em cima já faz esse trabalho.