from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.files.storage import default_storage
from accounts.jwt_auth import JWTAuthentication
from rest_framework.decorators import authentication_classes

from .models import File, Folder
from .serializers import FileSerializer, FolderSerializer


@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_files(request):
    folder_id = request.GET.get("folder")

    if folder_id:
        files = File.objects.filter(folder_id=folder_id)
    else:
        files = File.objects.filter(folder__isnull=True)

    return Response(FileSerializer(files, many=True).data)


@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_folders(request):
    folders = Folder.objects.filter(owner=request.user)
    return Response(FolderSerializer(folders, many=True).data)


@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_folder(request):
    name = request.data.get("name")
    folder = Folder.objects.create(name=name, owner=request.user)
    return Response(FolderSerializer(folder).data)


@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def upload_file(request):
    uploaded_file = request.FILES["file"]
    category = request.POST.get("category")
    folder_id = request.POST.get("folder")

    file_obj = File.objects.create(
        name=uploaded_file.name,
        file=uploaded_file,
        size=f"{round(uploaded_file.size / 1024 / 1024, 2)} MB",
        type=uploaded_file.name.split(".")[-1],
        category=category,
        uploaded_by=request.user,
        folder_id=folder_id if folder_id != "null" else None
    )

    return Response(FileSerializer(file_obj).data)


@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def move_file(request):
    file_id = request.data.get("file_id")
    folder_id = request.data.get("folder_id")

    file = File.objects.get(id=file_id)
    file.folder_id = folder_id if folder_id != "root" else None
    file.save()

    return Response({"status": "ok"})


@api_view(["DELETE"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_file(request, file_id):
    file = File.objects.get(id=file_id)
    file.delete()
    return Response({"status": "deleted"})
