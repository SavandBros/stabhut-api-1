from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from column.models import Column
from column.serializers import ColumnSerializer, ColumnRetrieveSerializer
from stabhut.utils import IsOrganizationOwnerOrReadOnly


class ColumnViewSet(viewsets.ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    permission_classes = (IsAuthenticated, IsOrganizationOwnerOrReadOnly,)
    filterset_fields = ('project', 'project__organization',)

    def get_queryset(self):
        return self.queryset.filter(project__organization__user=self.request.user)

    def get_serializer_class(self):
        if self.action is 'retrieve':
            return ColumnRetrieveSerializer
        return self.serializer_class
