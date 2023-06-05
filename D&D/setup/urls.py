from django.contrib import admin
from django.urls import path, include
from apps.characters.views import CharactersViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('characters', CharactersViewSet, basename='Characters')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
