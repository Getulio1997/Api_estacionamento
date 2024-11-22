from django.db import models

class Medida(models.Model):
    descricao = models.CharField(max_length=100)
    comprimento = models.CharField(max_length=50)
    criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descricao