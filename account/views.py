from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from account.serializers import UserSerializer
from stabhut.utils import StandardPagination, IsOwnerOrReadOnly


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):
    queryset = User.objects.all()
    pagination_class = StandardPagination
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    lookup_field = 'username'


def jwt_response_payload_handler(token, user=None, request=None) -> dict:
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }
