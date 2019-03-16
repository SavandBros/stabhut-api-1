from rest_framework import serializers

from column.models import Column
from project.serializers import ProjectSerializer


class ColumnSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()

    class Meta:
        model = Column
        fields = '__all__'


class ColumnWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = (
            'project',
            'name',
        )
