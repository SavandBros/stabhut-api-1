from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.v1.stabber.serializers import (
    CardSerializer,
    ColumnSerializer,
    LabelObjectSerializer,
    LabelSerializer,
    MilestoneSerializer,
    OrganizationSerializer,
    ProjectSerializer,
    TaskSerializer,
    TaskWriteSerializer,
    ChatWriteSerializer,
    ChatSerializer,
)
from api.v1.utils import IsOrganizationOwnerOrReadOnly, IsOwnerOrReadOnly
from stabber.models import Card, Column, Label, LabelObject, Milestone, Organization, Project, Task, Chat


class MilestoneViewSet(viewsets.ModelViewSet):
    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializer
    permission_classes = (IsOrganizationOwnerOrReadOnly,)
    filterset_fields = (
        "project",
        "closed",
    )


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (
        IsAuthenticated,
        IsOrganizationOwnerOrReadOnly,
    )
    filterset_fields = ("column", "column__project", "milestone", "epic", "is_epic")

    def get_queryset(self):
        return self.queryset.filter(column__project__organization__user=self.request.user)


class ColumnViewSet(viewsets.ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    permission_classes = (
        IsAuthenticated,
        IsOrganizationOwnerOrReadOnly,
    )
    filterset_fields = ("project",)

    def get_queryset(self):
        return self.queryset.filter(project__organization__user=self.request.user)


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    permission_classes = (
        IsAuthenticated,
        IsOrganizationOwnerOrReadOnly,
    )
    serializer_class = LabelSerializer
    filter_fields = ("organization",)

    def get_queryset(self):
        return self.queryset.filter(organization__user=self.request.user)


class LabelObjectViewSet(viewsets.ModelViewSet):
    queryset = LabelObject.objects.all()
    permission_classes = (IsOrganizationOwnerOrReadOnly,)
    serializer_class = LabelObjectSerializer
    filter_fields = ("kind", "to")


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = (
        IsAuthenticated,
        IsOwnerOrReadOnly,
    )

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (
        IsAuthenticated,
        IsOrganizationOwnerOrReadOnly,
    )
    filterset_fields = ("organization",)

    def get_queryset(self):
        return self.queryset.filter(organization__user=self.request.user)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = (
        IsAuthenticated,
        IsOrganizationOwnerOrReadOnly,
    )
    filterset_fields = ("project",)

    def get_queryset(self):
        return self.queryset.filter(project__organization__user=self.request.user)

    def get_serializer_class(self):
        if self.action in ["create", "update"]:
            return TaskWriteSerializer
        return TaskSerializer


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    permission_classes = (
        IsAuthenticated,
        IsOrganizationOwnerOrReadOnly,
    )
    filterset_fields = ("project",)

    def get_queryset(self):
        return self.queryset.filter(project__organization__user=self.request.user)

    def get_serializer_class(self):
        if self.action in ["create", "update"]:
            return ChatWriteSerializer
        return ChatSerializer
