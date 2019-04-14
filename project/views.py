from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from project.models import Project
from project.serializers import ProjectSerializer, ProjectWriteSerializer
from stabhut.utils import IsOrganizationOwnerOrReadOnly


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = (IsAuthenticated, IsOrganizationOwnerOrReadOnly,)
    filterset_fields = ('organization',)

    def get_queryset(self):
        return self.queryset.filter(organization__user=self.request.user)

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return ProjectWriteSerializer
        return ProjectSerializer
