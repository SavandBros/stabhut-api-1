from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from milestone.models import Milestone


class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = '__all__'
        extra_kwargs = {
            'organization': {'write_only': True}
        }

    def update(self, instance, data):
        if 'organization' in data and data.get('organization') != instance.organization:
            raise ValidationError({'organization': ['This field can not be updated.']})
        if data.get('project', None) is not None and data.get('project').organization != instance.organization:
            raise ValidationError({'project': ['This project does not belong to this organization.']})
        return super().update(instance, data)

    def create(self, data):
        if data.get('project', None) is not None and data.get('project').organization != data.get('organization'):
            raise ValidationError({'project': ['This project does not belong to this organization.']})
        return super().create(data)
