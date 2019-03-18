from rest_framework import serializers

from project.serializers import ProjectSerializer
from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()

    class Meta:
        model = Task
        fields = '__all__'


class TaskWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
