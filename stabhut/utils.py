from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination


class ObjectType:
    """
    Object types used for FKs for other models, like Label
    More will be added.
    """
    CARD = 1


OBJECT_TYPE_CHOICES = (
    (ObjectType.CARD, 'Card'),
)


class StandardPagination(PageNumberPagination):
    page_size_query_param = 'limit'
    page_size = 100


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):

        # Read permissions are allowed to any request safe request (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed for authenticated users
        if not request.user.is_authenticated:
            return False

        # Write permissions are only allowed to the owner of this object
        if type(obj) is not User:
            return obj.user == request.user

        # Write permissions are only allowed to the authenticated user
        return obj == request.user


class IsOrganizationOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of organization to edit it.
    """

    def has_object_permission(self, request, view, obj):

        # Read permissions are allowed to any request safe request (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed for authenticated users
        if not request.user.is_authenticated:
            return False

        # Write permissions are only allowed to the owner of the organization
        return obj.organization.user == request.user
