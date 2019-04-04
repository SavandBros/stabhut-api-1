from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from organization.models import Organization
from organization.serializers import OrganizationSerializer
from stabhut.utils import IsOwnerOrReadOnly


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
