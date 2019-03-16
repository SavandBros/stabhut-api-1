from rest_framework import serializers

from organization.serializers import OrganizationSerializer
from project.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()

    class Meta:
        model = Project
        fields = '__all__'


class ProjectWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'organization',
            'name',
        )
