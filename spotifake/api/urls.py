from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtistaViewSet, AlbumViewSet, MusicaViewSet

router = DefaultRouter()
router.register(r'artistas', ArtistaViewSet)
router.register(r'albuns', AlbumViewSet)
router.register(r'musicas', MusicaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]