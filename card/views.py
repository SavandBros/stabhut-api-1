from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from card.models import Card
from card.serializers import CardSerializer, CardRetrieveSerializer
from stabhut.utils import IsOrganizationOwnerOrReadOnly


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (IsAuthenticated, IsOrganizationOwnerOrReadOnly,)
    filterset_fields = ('column', 'column__project', 'milestone', 'epic', 'is_epic')

    def get_queryset(self):
        return self.queryset.filter(column__project__organization__user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CardRetrieveSerializer
        return self.serializer_class
