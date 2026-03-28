from django.db import models

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

# === CLASSE EVENTO (AGORA FORA DO PROJETO) ===
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
        # Aqui mudei um detalhe: o strftime pode dar erro se não formatar direto
        return f"{self.titulo}"

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ['data_evento']