from rest_framework import serializers

from chat.models import Chat


class ChatSerializer(serializers.ModelSerializer):
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
