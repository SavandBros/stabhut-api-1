from rest_framework import serializers

from column.models import Column


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = '__all__'
        extra_kwargs = {
            'project': {'write_only': True},
        }
