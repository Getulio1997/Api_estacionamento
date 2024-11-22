from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    id_administrador = models.ForeignKey('administrador', on_delete=models.CASCADE, null=True, blank=True, db_column='id_administrador')

    def __str__(self):
        return self.nome