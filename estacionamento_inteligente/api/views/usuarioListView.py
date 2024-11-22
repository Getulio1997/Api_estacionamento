from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models.usuario import Usuario
from api.serializers.usuario_serializer import UsuarioSerializer

class UsuarioListView(APIView):
    def get(self, request, id=None):
        if id is not None:
            # Buscar um usuário específico pelo id
            try:
                usuario = Usuario.objects.get(id=id)
                serializer = UsuarioSerializer(usuario)
                return Response(serializer.data)
            except Usuario.DoesNotExist:
                return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Se não passar o id, retorna todos os usuários
            usuarios = Usuario.objects.all()
            serializer = UsuarioSerializer(usuarios, many=True)
            return Response(serializer.data)
