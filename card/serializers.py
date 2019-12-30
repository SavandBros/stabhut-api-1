from typing import List

from rest_framework import serializers

from card.models import Card
from column.serializers import ColumnSerializer
from label.models import LabelObject


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

    def get_labels(self, obj) -> List[int]:
        labels = LabelObject.objects.filter(kind=LabelObject.Kind.CARD, to=obj.id)
        return labels.values_list("id", flat=True)


class CardRetrieveSerializer(CardSerializer):
    column = ColumnSerializer()
