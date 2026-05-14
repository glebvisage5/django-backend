from django.contrib import admin
from django.urls import path, include
from crm.views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/crm/', include('crm.urls')),
]
