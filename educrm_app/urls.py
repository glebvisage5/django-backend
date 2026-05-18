from django.urls import path
from .views import dashboard_page, tasks_page, files_page

urlpatterns = [
    path('', dashboard_page, name='educrm-dashboard'),
    path('tasks/', tasks_page, name='educrm-tasks'),
    path('files/', files_page, name='files_page'),
]
