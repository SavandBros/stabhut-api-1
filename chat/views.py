from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from chat.models import Chat
from chat.serializers import ChatSerializer, ChatWriteSerializer
from stabhut.utils import IsOrganizationOwnerOrReadOnly


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    permission_classes = (IsAuthenticated, IsOrganizationOwnerOrReadOnly,)
    filterset_fields = ('project',)

    def get_queryset(self):
        return self.queryset.filter(project__organization__user=self.request.user)

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return ChatWriteSerializer
        return ChatSerializer
