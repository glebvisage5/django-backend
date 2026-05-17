from django.urls import path
from . import api_views

urlpatterns = [
    path("tasks/", api_views.tasks_list),
    path("tasks/<int:pk>/", api_views.task_detail),
    path("tasks/<int:pk>/progress/", api_views.task_update_progress),
    path("tasks/<int:pk>/complete/", api_views.task_mark_complete),
    path("tasks/<int:pk>/comment/", api_views.task_add_comment),
    path("tasks/<int:pk>/upload/", api_views.task_upload_file),
]
