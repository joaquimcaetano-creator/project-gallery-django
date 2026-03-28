from django.shortcuts import render, get_object_or_404
from .models import Projeto
from django.db.models import Q

def home(request):
    # Esta é a página de boas-vindas que você queria
    return render(request, 'mostra/home.html')

def projetos(request):
    # Esta é a página que tem os cards e a busca
    termo_busca = request.GET.get('busca')
    if termo_busca:
        lista_projetos = Projeto.objects.filter(
            Q(titulo__icontains=termo_busca) | 
            Q(autor__icontains=termo_busca) |
            Q(resumo__icontains=termo_busca)
        )
    else:
        lista_projetos = Projeto.objects.all().order_by('-data_cadastro')
        
    return render(request, 'mostra/projetos.html', {'projetos': lista_projetos})

def detalhe(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    return render(request, 'mostra/detalhe_projeto.html', {'projeto': projeto})

def sobre(request):
    return render(request, 'mostra/sobre.html') 