from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projetos/', views.projetos, name='projetos'),
    path('projeto/<int:id>/', views.detalhe, name='detalhe'),
    path('sobre/', views.sobre, name='sobre'),





]