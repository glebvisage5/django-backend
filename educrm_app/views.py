from django.shortcuts import render

def dashboard_page(request):
    return render(request, "educrm/dashboard.html")

def tasks_page(request):
    return render(request, "educrm/tasks.html")

def files_page(request):
    return render(request, "educrm/files.html")