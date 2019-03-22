from rest_framework import viewsets

from label.models import Label, ObjectLabel
from label.serializers import LabelSerializer, LabelWriteSerializer, ObjectLabelSerializer
from stabhut.utils import IsOrganizationOwnerOrReadOnly


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    permission_classes = (IsOrganizationOwnerOrReadOnly,)

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return LabelWriteSerializer
        return LabelSerializer


class ObjectLabelViewSet(viewsets.ModelViewSet):
    queryset = ObjectLabel.objects.all()
    permission_classes = (IsOrganizationOwnerOrReadOnly,)
    serializer_class = ObjectLabelSerializer
