from django.shortcuts import render

# Página Inicial
def home(request):
    return render(request, 'mostra/home.html')

from .models import Projeto # Importe o modelo no topo

def projetos(request):
    lista_projetos = Projeto.objects.all() # Busca todos os projetos do banco
    return render(request, 'mostra/projetos.html', {'projetos': lista_projetos})

# Detalhes de um Projeto (por enquanto continua simples, pois precisa do banco de dados)
def detalhe(request, id):
    # Usamos f-string para passar o ID para o template no futuro
    return render(request, 'mostra/detalhe.html', {'id': id})

# Página Sobre a Mostra (vai ler o arquivo sobre.html)
def sobre(request):
    return render(request, 'mostra/sobre.html')