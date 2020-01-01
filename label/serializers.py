from rest_framework import serializers

from label.models import Label, LabelObject


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = '__all__'
        extra_kwargs = {
            'organization': {'write_only': True},
        }


class LabelObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabelObject
        fields = '__all__'


class LabelObjectMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabelObject
        fields = (
            'id',
            'label',
        )
