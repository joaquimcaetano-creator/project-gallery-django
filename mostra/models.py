from django.db import models

class Projeto(models.Model):
    # Áreas de conhecimento (MANTIDAS EXATAMENTE COMO VOCÊ FEZ)
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
    
    # Campo de imagem que você já tinha (ajustei apenas para organizar em subpasta)
    imagem = models.ImageField(upload_to='projetos/fotos/', null=True, blank=True)
    
    # --- NOVOS CAMPOS PARA INTERATIVIDADE ---
    arquivo_pdf = models.FileField(upload_to='projetos/pdfs/', null=True, blank=True, help_text="Upload do artigo ou banner")
    link_externo = models.URLField(max_length=500, null=True, blank=True, help_text="Link para vídeo no YouTube ou site")
    # ----------------------------------------

    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo