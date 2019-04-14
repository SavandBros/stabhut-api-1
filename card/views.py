from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from card.models import Card
from card.serializers import CardSerializer
from stabhut.utils import IsOrganizationOwnerOrReadOnly


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (IsAuthenticated, IsOrganizationOwnerOrReadOnly,)
    filterset_fields = ('column', 'column__project',)

    def get_queryset(self):
        return self.queryset.filter(column__project__organization__user=self.request.user)
