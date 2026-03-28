from django.contrib import admin
from .models import Projeto, Evento, LinhaPesquisa, Participante  # Adicionado Participante aqui!

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

# --- Configuração dos Participantes (Inline) ---
class ParticipanteInline(admin.TabularInline):
    model = Participante
    extra = 1  # Deixa um espaço em branco para adicionar novo membro rápido
    fields = ('nome', 'cargo', 'foto')  # Garante que esses campos apareçam

# --- Registro da Linha de Pesquisa com os Participantes ---
@admin.register(LinhaPesquisa)
class LinhaPesquisaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'cor_card')
    search_fields = ('titulo',)
    inlines = [ParticipanteInline]  # Isso permite cadastrar a equipe dentro da pesquisa

# Opcional: Registrar Participante sozinho também (caso precise editar fotos isoladas)
@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'linha')
    list_filter = ('linha',)