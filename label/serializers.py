from rest_framework import serializers

from label.models import Label, LabelObject


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = (
            'id',
            'name',
            'color',
        )


class LabelObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabelObject
        fields = '__all__'
