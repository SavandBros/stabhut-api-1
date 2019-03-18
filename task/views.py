from rest_framework import viewsets

from stabhut.utils import IsOrganizationOwnerOrReadOnly
from task.models import Task
from task.serializers import TaskSerializer, TaskWriteSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = (IsOrganizationOwnerOrReadOnly,)

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return TaskWriteSerializer
        return TaskSerializer
