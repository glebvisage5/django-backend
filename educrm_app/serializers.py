from rest_framework import serializers
from .models import Task, TaskComment


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "course",
            "status",
            "priority",
            "progress",
            "due_date",
            "created_at",
        ]


class TaskCommentSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = TaskComment
        fields = [
            "id",
            "task",
            "author",
            "author_name",
            "text",
            "created_at",
        ]
