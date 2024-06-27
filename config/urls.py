
from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from livraria.views import CategoriaViewSet
from livraria.views import EditoraViewSet
from livraria.views import AutorViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"editoras", EditoraViewSet)
router.register(r"autor", AutorViewSet) 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls))
]
