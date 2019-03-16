from rest_framework import viewsets

from project.models import Project
from project.serializers import ProjectSerializer, ProjectWriteSerializer
from stabhut.utils import IsOrganizationOwnerOrReadOnly


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = (IsOrganizationOwnerOrReadOnly,)

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return ProjectWriteSerializer
        return ProjectSerializer
