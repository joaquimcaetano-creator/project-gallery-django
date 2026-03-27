from django.shortcuts import render

# Página Inicial
def home(request):
    return render(request, 'mostra/home.html')

# Lista de Projetos (vai ler o arquivo projetos.html)
def projetos(request):
    return render(request, 'mostra/projetos.html')

# Detalhes de um Projeto (por enquanto continua simples, pois precisa do banco de dados)
def detalhe(request, id):
    # Usamos f-string para passar o ID para o template no futuro
    return render(request, 'mostra/detalhe.html', {'id': id})

# Página Sobre a Mostra (vai ler o arquivo sobre.html)
def sobre(request):
    return render(request, 'mostra/sobre.html')