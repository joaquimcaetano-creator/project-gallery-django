from django.db import models

class Projeto(models.Model):
    # Opções para o administrador escolher
    AREAS_CHOICES = [
        ('TEC', 'Tecnologia'),
        ('SAU', 'Saúde'),
        ('EDU', 'Educação'),
        ('HUM', 'Humanas'),
    ]

    titulo = models.CharField(max_length=200)
    resumo = models.TextField()
    area = models.CharField(max_length=3, choices=AREAS_CHOICES, default='TEC') # Novo campo!
    autor = models.CharField(max_length=150)
    orientador = models.CharField(max_length=150)
    imagem = models.ImageField(upload_to='projetos/', null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
        return self.titulo