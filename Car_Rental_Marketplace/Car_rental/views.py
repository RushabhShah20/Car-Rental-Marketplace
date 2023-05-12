from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# from .forms import UserLoginForm

# from .forms import LoginForm

# from .serializers import UserSerializer


# Create your views here.
def index(request):
    return render(request, "index.html")


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        User.objects.create_user(username=username, password=password, email=email)
        messages.success(request, "Your account has been created!")
        return redirect("login")
    return render(request, "signup.html")


def login(request):
    # if request.method == "POST":
    #     form = UserLoginForm(request=request, data=request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data.get("username")
    #         password = form.cleaned_data.get("password")
    #         user = authenticate(request, username=username, password=password)
    #         if user is not None:
    #             login(request, user)
    #             return redirect("home")
    # else:
    #     form = UserLoginForm()
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


print("The database being used is:", connection.vendor)
