from django.urls import path
from .dashboard import dashboard_api

urlpatterns = [
    path('dashboard/', dashboard_api, name='educrm-dashboard-api'),
]
