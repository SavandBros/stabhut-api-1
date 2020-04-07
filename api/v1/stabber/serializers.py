from rest_framework import serializers

from account.serializers import UserSerializer
from stabber.models import Card, Column, Label, LabelObject, Milestone, Organization, Project, Task, Chat


class CardSerializer(serializers.ModelSerializer):
    labels = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Card
        fields = (
            "id",
            "title",
            "column",
            "content",
            "assignee",
            "epic",
            "is_epic",
            "milestone",
            "points",
            "points_estimate",
            "order",
            "created",
            "updated",
            "labels",
        )

    def get_labels(self, obj):
        serializer = LabelObjectMinimalSerializer(
            data=LabelObject.objects.filter(kind=LabelObject.Kind.CARD, to=obj.id), many=True
        )
        serializer.is_valid()
        return serializer.data


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = "__all__"


class CardRetrieveSerializer(CardSerializer):
    column = ColumnSerializer()


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = "__all__"
        extra_kwargs = {
            "organization": {"write_only": True},
        }


class LabelObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabelObject
        fields = "__all__"


class LabelObjectMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabelObject
        fields = (
            "id",
            "label",
        )


class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = "__all__"


class OrganizationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Organization
        fields = "__all__"

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
        extra_kwargs = {
            "organization": {"write_only": True},
        }


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "id",
            "content",
            "checked",
        )


class TaskWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = (
            "id",
            "user",
            "content",
            "created",
        )


class ChatWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = (
            "project",
            "content",
        )

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
