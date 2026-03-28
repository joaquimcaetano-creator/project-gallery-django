from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.utils import timezone
from .models import Projeto, Evento, LinhaPesquisa

# --- PÁGINA INICIAL ---
def home(request):
    return render(request, 'mostra/home.html')

# --- REPOSITÓRIO DE PROJETOS (COM BUSCA) ---
def projetos(request):
    termo_busca = request.GET.get('busca')
    if termo_busca:
        lista_projetos = Projeto.objects.filter(
            Q(titulo__icontains=termo_busca) | 
            Q(autor__icontains=termo_busca) |
            Q(resumo_curto__icontains=termo_busca)
        ).order_by('-data_cadastro')
    else:
        lista_projetos = Projeto.objects.all().order_by('-data_cadastro')
        
    return render(request, 'mostra/projetos.html', {'projetos': lista_projetos})

# --- DETALHES DE UM PROJETO ESPECÍFICO ---
def detalhe(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    return render(request, 'mostra/detalhe_projeto.html', {'projeto': projeto})

# --- LINHAS DE PESQUISA (NOVA ABA) ---
def pesquisas(request):
    linhas = LinhaPesquisa.objects.all()
    return render(request, 'mostra/pesquisas.html', {'linhas': linhas})

# --- AGENDA DE EVENTOS (FILTRA O QUE AINDA VAI ACONTECER) ---
def agenda(request):
    # Pega apenas eventos de "agora" para o futuro
    proximos_eventos = Evento.objects.filter(data_evento__gte=timezone.now()).order_by('data_evento')
    return render(request, 'mostra/agenda.html', {'eventos': proximos_eventos})

# --- PÁGINA SOBRE ---
def sobre(request):
    return render(request, 'mostra/sobre.html')