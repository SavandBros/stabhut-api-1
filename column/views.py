from rest_framework import viewsets

from column.models import Column
from column.serializers import ColumnSerializer
from stabhut.utils import IsOrganizationOwnerOrReadOnly


class ColumnViewSet(viewsets.ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    permission_classes = (IsOrganizationOwnerOrReadOnly,)
    filterset_fields = ('project',)
