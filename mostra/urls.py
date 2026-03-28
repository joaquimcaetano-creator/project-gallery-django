from django.urls import path
from . import views

urlpatterns = [
    # Páginas Principais
    path('', views.home, name='home'),
    path('projetos/', views.projetos, name='projetos'),
    path('pesquisas/', views.pesquisas, name='pesquisas'), # Nova aba que criamos
    path('agenda/', views.agenda, name='agenda'),
    path('sobre/', views.sobre, name='sobre'),
    
    # Detalhes do Projeto (ID dinâmico)
    path('projeto/<int:id>/', views.detalhe, name='detalhe'),

path('pesquisa/<int:id>/', views.detalhe_pesquisa, name='detalhe_pesquisa'),


]