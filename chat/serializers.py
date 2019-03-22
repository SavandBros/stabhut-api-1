from rest_framework import serializers

from account.serializers import UserSerializer
from chat.models import Chat
from project.serializers import ProjectSerializer


class ChatSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()
    user = UserSerializer()

    class Meta:
        model = Chat
        fields = '__all__'


class ChatWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = (
            'project',
            'content',
        )

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
