from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from label.models import Label, LabelObject
from label.serializers import LabelSerializer, LabelObjectSerializer
from stabhut.utils import IsOrganizationOwnerOrReadOnly


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    permission_classes = (IsAuthenticated, IsOrganizationOwnerOrReadOnly,)
    serializer_class = LabelSerializer
    filter_fields = ('organization',)
    lookup_field = 'name'

    def get_queryset(self):
        return self.queryset.filter(organization__user=self.request.user)


class LabelObjectViewSet(viewsets.ModelViewSet):
    queryset = LabelObject.objects.all()
    permission_classes = (IsOrganizationOwnerOrReadOnly,)
    serializer_class = LabelObjectSerializer
    filter_fields = ('kind', 'to')
