from rest_framework import serializers

from column.models import Column


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = (
            'project',
            'id',
            'name',
        )
        extra_kwargs = {
            'project': {'write_only': True},
        }


class ColumnRetrieveSerializer(ColumnSerializer):
    project = ProjectSerializer()
