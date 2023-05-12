from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from .models import Car_renter, Orders
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, "index.html")


def signup(request):
    if request.method == "POST":
        try:
            email = request.POST["email"]
            phone_number = request.POST["phone-number"]
            username = request.POST["username"]
            print(username)
            password = request.POST["password"]
            print(password)
            confirm_password = request.POST["confirm-password"]
        except MultiValueDictKeyError:
            error_message = "Please fill all fields"
            return render(request, "signup.html", {"error_message": error_message})
        user = Car_renter.objects.filter(
            username=username, phone_number=phone_number, password=password, email=email
        )
        if user.exists():
            error_message1 = "Car renter already exists"
            print(error_message1)
            return render(request, "signup.html", {"error_message": error_message1})
        if confirm_password != password:
            error_message2 = "Password and Confirm password do not match"
            print(error_message2)
            return render(request, "signup.html", {"error_message": error_message2})
        user1 = Car_renter(
            phone_number=phone_number,
            username=username,
            email=email,
            password=password,
        )
        user1.save()
        messages.success(request, "Your account has been created!")
        return redirect("login")
    return render(request, "signup.html")


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = Car_renter.objects.filter(email=email, password=password).first()
        if user:
            return redirect("/dashboard")
        else:
            error_message = "Invaild email or password"
            return render(request, "login.html", {"error_message": error_message})
        try:
            user = Car_renter.objects.get(email=email)
            passw = Car_renter.objects.get(password=password, email=email)
            if not passw:
                raise Car_renter.DoesNotExist
        except Car_renter.DoesNotExist:
            error_message = "Invalid email or password"
            return render(request, "login.html", {"error_message": error_message})
        return redirect("/dashboard")
    else:
        return render(request, "login.html")


def logout(request):
    logout(request)
    return redirect("index.html")


def about(request):
    return render(request, "about.html")


# @api_view(["POST"])
# def create_user(request):
#     serializer = Car_renterSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"user_id": serializer.instance.id}, status=201)
#     else:
#         return Response(serializer.errors, status=400)


def dashboard(request):
    context = {}
    return render(request, "dashboard.html", context)


print("The database being used is:", connection.vendor)
