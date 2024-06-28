from rest_framework.viewsets import ModelViewSet

from livraria.models import Livro
from livraria.serializers import LivroSerializer
from livraria.serializers import LivroDetailSerializer
from livraria.serializers import LivroListSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    
    def get_serializer_class(self):
        if self.action in "retrieve":
            return LivroDetailSerializer
        elif self.action == "list":
            return LivroListSerializer
        return LivroSerializer