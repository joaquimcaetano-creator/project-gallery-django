from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projetos/', views.projetos, name='projetos'),
    path('sobre/', views.sobre, name='sobre'),
    # Verifique se esta linha abaixo existe:
    path('projeto/<int:id>/', views.detalhe, name='detalhe_projeto'),
]