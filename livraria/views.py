from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from livraria.models import Categoria
from livraria.serializers import CategoriaSerializer
from livraria.models import Editora
from livraria.serializers import EditoraSerializer
from livraria.models import Autor
from livraria.serializers import AutorSerializer
from livraria.models import Livro
from livraria.serializers import LivroSerializer
from livraria.serializers import LivroDetailSerializer
from livraria.serializers import LivroListSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    
    def get_serializer_class(self):
        if self.action in "retrieve":
            return LivroDetailSerializer
        elif self.action == "list":
            return LivroListSerializer
        return LivroSerializer