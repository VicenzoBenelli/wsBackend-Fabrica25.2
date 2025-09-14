from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register(r'Filme', FilmeViewSet, basename='filme')
router.register(r'Resenha', ResenhaViewSet, basename='resenha')
router.register(r'CustomUser', CustomUserViewSet, basename="usuario")

urlpatterns = router.urls   