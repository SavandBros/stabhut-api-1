from rest_framework import serializers

from account.serializers import UserSerializer
from card.models import Card
from column.serializers import ColumnSerializer


class CardSerializer(serializers.ModelSerializer):
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
        )


class CardRetrieveSerializer(CardSerializer):
    column = ColumnSerializer()
    assignee = UserSerializer()
