from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Task, TaskComment
from .serializers import TaskSerializer, TaskCommentSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def tasks_list(request):
    tasks = Task.objects.all().order_by("due_date")
    return Response({"tasks": TaskSerializer(tasks, many=True).data})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def task_detail(request, pk):
    task = Task.objects.get(id=pk)
    return Response(TaskSerializer(task).data)


@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def task_update_progress(request, pk):
    task = Task.objects.get(id=pk)
    task.progress = request.data.get("progress", task.progress)
    if task.progress >= 100:
        task.status = "completed"
    task.save()
    return Response(TaskSerializer(task).data)


@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def task_mark_complete(request, pk):
    task = Task.objects.get(id=pk)
    task.status = "completed"
    task.progress = 100
    task.save()
    return Response(TaskSerializer(task).data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def task_add_comment(request, pk):
    task = Task.objects.get(id=pk)
    comment = TaskComment.objects.create(
        task=task,
        author=request.user,
        text=request.data.get("text")
    )
    return Response(TaskCommentSerializer(comment).data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def task_upload_file(request, pk):
    task = Task.objects.get(id=pk)
    file = request.FILES.get("file")

    if not file:
        return Response({"error": "No file provided"}, status=400)

    path = f"uploads/tasks/{task.id}/{file.name}"
    import os
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)

    task.attachments.append(file.name)
    task.save()

    return Response({"filename": file.name})
