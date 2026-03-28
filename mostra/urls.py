from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),            # Página de Início (Vazia/Bem-vindo)
    path('projetos/', views.projetos, name='projetos'), # Página com os cards e busca
    path('projeto/<int:id>/', views.detalhe, name='detalhe'),
    path('sobre/', views.sobre, name='sobre'),
]