from django.contrib import admin
from django.urls import path, include
from apps.escola.views import AlunosViewSet, CursosViewSet, MatriculasViewsSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matriculas', MatriculasViewsSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('escola/', include('escola.urls'))
]
