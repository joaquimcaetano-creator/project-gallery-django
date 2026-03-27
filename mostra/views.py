from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Página Inicial da Mostra</h1><p>Bem-vindo ao portal!</p>")

def projetos(request):
    return HttpResponse("<h1>Lista de Projetos</h1><p>Aqui aparecerão os trabalhos acadêmicos.</p>")

def detalhe(request, id):
    return HttpResponse(f"<h1>Detalhes do Projeto {id}</h1><p>Informações específicas do projeto.</p>")

def sobre(request):
    return HttpResponse("<h1>Sobre a Mostra Virtual</h1><p>Projeto desenvolvido para a UFJ.</p>")