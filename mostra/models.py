from django.db import models

class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    resumo = models.TextField()
    autor = models.CharField(max_length=150)
    orientador = models.CharField(max_length=150)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
