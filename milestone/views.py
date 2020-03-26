from rest_framework.viewsets import ModelViewSet

from milestone.models import Milestone
from milestone.serializer import MilestoneSerializer
from stabhut.utils import IsOrganizationOwnerOrReadOnly


class MilestoneViewSet(ModelViewSet):
    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializer
    permission_classes = (IsOrganizationOwnerOrReadOnly,)
    filterset_fields = ('project', 'closed',)
