from rest_framework import viewsets

from card.models import Card
from card.serializers import CardWriteSerializer, CardSerializer
from stabhut.utils import IsOrganizationOwnerOrReadOnly


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    permission_classes = (IsOrganizationOwnerOrReadOnly,)

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return CardWriteSerializer
        return CardSerializer
