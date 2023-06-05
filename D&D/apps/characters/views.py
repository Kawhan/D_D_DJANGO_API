from rest_framework import viewsets
from characters.models import Character
from characters.serializer import CharacterSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class CharactersViewSet(viewsets.ModelViewSet):
    """ List all Characters in API

    Args:
        None
    """

    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
