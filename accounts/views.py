from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from crm.models import Student
from .utils import create_jwt, decode_jwt
import json


@csrf_exempt
def register_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "Метод не поддерживается"}, status=405)

    data = json.loads(request.body)

    name = data.get("name")
    email = data.get("email")
    group = data.get("institution")
    password = data.get("password")
    confirm = data.get("confirmPassword")

    if not all([name, email, group, password, confirm]):
        return JsonResponse({"error": "Заполните все поля."}, status=400)

    if password != confirm:
        return JsonResponse({"error": "Пароли не совпадают."}, status=400)

    if User.objects.filter(email=email).exists():
        return JsonResponse({"error": "Пользователь с таким email уже существует."}, status=400)

    user = User.objects.create(
        username=email,
        email=email,
        first_name=name,
        password=make_password(password)
    )

    Student.objects.create(
        user=user,
        group=group
    )

    return JsonResponse({"message": "Регистрация успешна"}, status=201)


@csrf_exempt
def login_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "Метод не поддерживается"}, status=405)

    data = json.loads(request.body)

    email = data.get("email")
    password = data.get("password")

    user = authenticate(username=email, password=password)

    if user is None:
        return JsonResponse({"error": "Неверный email или пароль"}, status=401)
    
    login(request, user)

    token = create_jwt(user.id)

    return JsonResponse({
        "message": "Успешный вход",
        "token": token,
        "user": {
            "id": user.id,
            "name": user.first_name,
            "email": user.email,
            "is_admin": user.is_staff
        }
    })


def me_view(request):
    auth = request.headers.get("Authorization")

    if not auth or not auth.startswith("Bearer "):
        return JsonResponse({"error": "Токен отсутствует"}, status=401)

    token = auth.split(" ")[1]
    payload = decode_jwt(token)

    if not payload:
        return JsonResponse({"error": "Неверный или истёкший токен"}, status=401)

    user = User.objects.get(id=payload["user_id"])

    return JsonResponse({
        "id": user.id,
        "name": user.first_name,
        "email": user.email,
        "is_admin": user.is_staff
    })
