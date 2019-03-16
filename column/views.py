from rest_framework import viewsets

from column.models import Column
from column.serializers import ColumnWriteSerializer, ColumnSerializer
from stabhut.utils import IsOrganizationOwnerOrReadOnly


class ColumnViewSet(viewsets.ModelViewSet):
    queryset = Column.objects.all()
    permission_classes = (IsOrganizationOwnerOrReadOnly,)

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return ColumnWriteSerializer
        return ColumnSerializer
