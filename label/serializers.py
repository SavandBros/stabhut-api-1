from rest_framework import serializers

from label.models import Label, ObjectLabel
from organization.serializers import OrganizationSerializer


class LabelSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()

    class Meta:
        model = Label
        fields = '__all__'


class LabelWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = '__all__'


class ObjectLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectLabel
        fields = '__all__'
