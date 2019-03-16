from rest_framework import serializers

from card.models import Card
from column.serializers import ColumnSerializer


class CardSerializer(serializers.ModelSerializer):
    column = ColumnSerializer()

    class Meta:
        model = Card
        fields = '__all__'


class CardWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'
