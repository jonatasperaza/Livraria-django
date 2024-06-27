from rest_framework.serializers import ModelSerializer

from livraria.models import Categoria
from livraria.models import Editora

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"