from rest_framework import serializers

from column.models import Column
from project.serializers import ProjectSerializer


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = (
            'id',
            'project',
            'name',
        )


class ColumnRetrieveSerializer(ColumnSerializer):
    project = ProjectSerializer()
