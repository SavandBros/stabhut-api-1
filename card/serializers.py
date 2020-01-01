from typing import List

from rest_framework import serializers

from card.models import Card
from column.serializers import ColumnSerializer
from label.models import LabelObject
from label.serializers import LabelObjectSerializer, LabelObjectMinimalSerializer


class CardSerializer(serializers.ModelSerializer):
    labels = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Card
        fields = (
            'id',
            'column',
            'content',
            'assignee',
            'order',
            'created',
            'updated',
            'labels',
        )

    def get_labels(self, obj):
        serializer = LabelObjectMinimalSerializer(
            data=LabelObject.objects.filter(kind=LabelObject.Kind.CARD, to=obj.id),
            many=True
        )
        serializer.is_valid()
        return serializer.data


class CardRetrieveSerializer(CardSerializer):
    column = ColumnSerializer()
