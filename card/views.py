from rest_framework import viewsets

from card.models import Card
from card.serializers import CardSerializer
from stabhut.utils import IsOrganizationOwnerOrReadOnly


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (IsOrganizationOwnerOrReadOnly,)
