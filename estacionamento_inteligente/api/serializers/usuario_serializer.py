from rest_framework import serializers
from api.models.usuario import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email', 'data_criacao', 'id_administrador']
