from rest_framework import viewsets, filters
from characters.models import Character
from characters.serializer import CharacterSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend


class CharactersViewSet(viewsets.ModelViewSet):
    """ List all Characters in API

    Args:
        None
    """

    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['race']
    search_fields = ['race', 'name']
    filterset_fields = ['race', 'name']
