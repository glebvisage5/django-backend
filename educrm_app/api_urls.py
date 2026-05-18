from django.urls import path
from . import api_views
from .views_files import (
    list_files, list_folders, create_folder,
    upload_file, move_file, delete_file
)

urlpatterns = [
    path("tasks/", api_views.tasks_list),
    path("tasks/<int:pk>/", api_views.task_detail),
    path("tasks/<int:pk>/progress/", api_views.task_update_progress),
    path("tasks/<int:pk>/complete/", api_views.task_mark_complete),
    path("tasks/<int:pk>/comment/", api_views.task_add_comment),
    path("tasks/<int:pk>/upload/", api_views.task_upload_file),

    path("dashboard/", api_views.dashboard),

    path("files/", list_files),
    path("folders/", list_folders),
    path("folders/create/", create_folder),
    path("files/upload/", upload_file),
    path("files/move/", move_file),
    path("files/delete/<int:file_id>/", delete_file),
]
