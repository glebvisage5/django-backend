from django.http import JsonResponse
from educrm_app.auth import get_user_from_request

def dashboard_api(request):
    user = get_user_from_request(request)

    if not user:
        return JsonResponse({"error": "Unauthorized"}, status=401)

    data = {
        "tasks": [],
        "events": [],
        "leaderboard": [],
        "deadlines": [],
        "performance": {}
    }

    return JsonResponse(data)
