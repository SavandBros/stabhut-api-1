from rest_framework import viewsets

from organization.models import Organization
from organization.serializers import OrganizationSerializer
from stabhut.utils import StandardPagination, IsOwnerOrReadOnly


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    pagination_class = StandardPagination
    serializer_class = OrganizationSerializer
    permission_classes = (IsOwnerOrReadOnly,)
