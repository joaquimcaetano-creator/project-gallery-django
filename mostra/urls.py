from django.urls import path
from . import views

urlpatterns = [
    # --- Páginas Principais (Listas) ---
    path('', views.home, name='home'),
    path('projetos/', views.projetos, name='projetos'),
    path('pesquisas/', views.pesquisas, name='pesquisas'),
    path('agenda/', views.agenda, name='agenda'),
    path('sobre/', views.sobre, name='sobre'),
    
    # --- Páginas de Detalhes (Individuais) ---
    # Detalhes de um Projeto
    path('projeto/<int:id>/', views.detalhe, name='detalhe'),
    
    # Detalhes de uma Linha de Pesquisa (A que faltava!)
    path('pesquisa/<int:id>/', views.detalhe_pesquisa, name='detalhe_pesquisa'),
]