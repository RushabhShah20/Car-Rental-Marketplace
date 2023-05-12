from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User

# from .forms import UserLoginForm

# from .forms import LoginForm

# from .serializers import UserSerializer


# Create your views here.
def index(request):
    return render(request, "index.html")


def signup(request):
    if request.method == "POST":
        try:
            phone_number = request.POST["phone-number"]
            username = request.POST["username"]
            password = request.POST["password"]
            confirm_password = request.POST["confirm-password"]
        except MultiValueDictKeyError:
            error_message = "Please fill all fields"
            return render(request, "signup.html", {"error_message": error_message})
        user = User.objects.filter(
            username=username, password=password, phone_number=phone_number
        )
        if user.exists():
            error_message1 = "User already exists"
            print(error_message1)
            return render(request, "signup.html", {"error_message": error_message1})
        if confirm_password != password:
            error_message2 = "Password and Confirm password do not match"
            print(error_message2)
            return render(request, "signup.html", {"error_message": error_message2})
        user = User.objects.create_user(
            password=password, phone_number=phone_number, username=username
        )
        messages.success(request, "Your account has been created!")
        return redirect("login")
    return render(request, "signup.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.filter(username=username, password=password).first()
        if user:
            return redirect("dashboard.html")
        else:
            error_message = "Invaild username or password"
            return render(request, "login.html", {"error_message": error_message})
    else:
        return render(request, "login.html")


def logout(request):
    logout(request)
    return redirect("index.html")


def about(request):
    return render(request, "about.html")


@api_view(["POST"])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"user_id": serializer.instance.id}, status=201)
    else:
        return Response(serializer.errors, status=400)


def dashboard(request):
    context = {}
    return render(request, "dashboard.html", context)


print("The database being used is:", connection.vendor)
