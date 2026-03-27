from django.shortcuts import render

# Página Inicial
def home(request):
    return render(request, 'mostra/home.html')

from .models import Projeto # Importe o modelo no topo

def projetos(request):
    lista_projetos = Projeto.objects.all() # Busca todos os projetos do banco
    return render(request, 'mostra/projetos.html', {'projetos': lista_projetos})

from django.shortcuts import render, get_object_or_404 # Adicione o get_object_or_404


# ... as outras views continuam iguais ...

def detalhe(request, id):
    # Isso busca o projeto pelo ID ou mostra uma página de erro 404 se não existir
    projeto = get_object_or_404(Projeto, pk=id)
    return render(request, 'mostra/detalhe.html', {'projeto': projeto})

# Página Sobre a Mostra (vai ler o arquivo sobre.html)
def sobre(request):
    return render(request, 'mostra/sobre.html')