from django.db import models

class Administrador(models.Model):
    idade = models.CharField(max_length=100)
    ano = models.CharField(max_length=100)
    cricao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.idade