from django.db import models

# === CLASSE PROJETO ===
class Projeto(models.Model):
    AREAS_CHOICES = [
        ('TEC', 'Tecnologia'),
        ('SAU', 'Saúde'),
        ('EDU', 'Educação'),
        ('HUM', 'Humanas'),
    ]

    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    orientador = models.CharField(max_length=150)
    
    resumo_curto = models.TextField(max_length=300, help_text="Aparece no card da lista", default='', blank=True)
    conteudo_completo = models.TextField(help_text="Descrição detalhada que aparece na página interna", default='', blank=True)
    
    area = models.CharField(max_length=3, choices=AREAS_CHOICES, default='TEC')
    
    imagem = models.ImageField(upload_to='projetos/fotos/', null=True, blank=True)
    
    arquivo_pdf = models.FileField(upload_to='projetos/pdfs/', null=True, blank=True, help_text="Upload do artigo ou banner")
    link_externo = models.URLField(max_length=500, null=True, blank=True, help_text="Link para vídeo no YouTube ou site")

    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


# === CLASSE EVENTO ===
class Evento(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título do Evento")
    descricao = models.TextField(verbose_name="Descrição")
    data_evento = models.DateTimeField(verbose_name="Data e Hora")
    local_ou_link = models.CharField(max_length=255, verbose_name="Local ou Link da Live")
    
    CATEGORIAS = [
        ('LIVE', 'Live/Webinário'),
        ('DEFESA', 'Defesa de TCC'),
        ('PALESTRA', 'Palestra/Workshop'),
    ]
    categoria = models.CharField(max_length=10, choices=CATEGORIAS, default='LIVE')

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ['data_evento']


# === CLASSE LINHA DE PESQUISA ===
class LinhaPesquisa(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título da Linha")
    descricao = models.TextField(
        verbose_name="Descrição Curta (Card)", 
        help_text="Aparece no card colorido da lista"
    )
    
    conteudo_detalhado = models.TextField(
        verbose_name="Conteúdo Completo", 
        blank=True, 
        null=True, 
        help_text="O texto detalhado que aparecerá na página interna da pesquisa"
    )
    
    situacao = models.CharField(
        max_length=100, 
        verbose_name="Situação", 
        default="Em execução", 
        help_text="Ex: Em andamento, Concluído, Planejamento"
    )
    
    cor_card = models.CharField(
        max_length=20, 
        default="#b8a2e7", 
        help_text="Cor em HEX (ex: #b8a2e7)"
    )

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Linha de Pesquisa"
        verbose_name_plural = "Linhas de Pesquisa"


# === NOVA CLASSE PARTICIPANTE ===
class Participante(models.Model):
    # Relaciona o participante a uma Linha de Pesquisa específica
    linha = models.ForeignKey(
        LinhaPesquisa, 
        on_delete=models.CASCADE, 
        related_name='participantes',
        verbose_name="Linha de Pesquisa"
    )
    
    nome = models.CharField(max_length=150, verbose_name="Nome Completo")
    cargo = models.CharField(
        max_length=100, 
        verbose_name="Cargo/Função", 
        help_text="Ex: Coordenador, Pesquisador, Bolsista"
    )
    
    foto = models.ImageField(
        upload_to='pesquisadores/fotos/', 
        null=True, 
        blank=True, 
        verbose_name="Foto de Perfil",
        help_text="Opcional. Se não enviar, um ícone padrão será exibido."
    )

    def __str__(self):
        return f"{self.nome} - {self.linha.titulo}"

    class Meta:
        verbose_name = "Participante"
        verbose_name_plural = "Participantes"