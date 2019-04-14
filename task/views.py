from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from stabhut.utils import IsOrganizationOwnerOrReadOnly
from task.models import Task
from task.serializers import TaskSerializer, TaskWriteSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated, IsOrganizationOwnerOrReadOnly,)

    def get_queryset(self):
        return self.queryset.filter(project__organization__user=self.request.user)

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return TaskWriteSerializer
        return TaskSerializer
