from rest_framework import serializers
from .models import Task, TaskComment, File, Folder


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

class FolderSerializer(serializers.ModelSerializer):
    files_count = serializers.SerializerMethodField()

    class Meta:
        model = Folder
        fields = ["id", "name", "created_at", "files_count"]

    def get_files_count(self, obj):
        return obj.file_set.count()


class FileSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.CharField(source="uploaded_by.first_name")

    class Meta:
        model = File
        fields = [
            "id", "name", "size", "type", "category",
            "uploaded_by", "uploaded_at", "folder"
        ]