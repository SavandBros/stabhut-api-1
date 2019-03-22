from rest_framework import viewsets

from chat.models import Chat
from chat.serializers import ChatSerializer, ChatWriteSerializer
from stabhut.utils import IsOrganizationOwnerOrReadOnly


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    permission_classes = (IsOrganizationOwnerOrReadOnly,)

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return ChatWriteSerializer
        return ChatSerializer
