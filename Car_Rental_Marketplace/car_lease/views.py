from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from .models import Car_leaser
from django.contrib import messages


# Create your views here.
def car_lease_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = Car_leaser.objects.filter(
            car_owner_email=email, car_owner_password=password
        ).first()
        if user:
            return redirect("/car_lease_dashboard")
        else:
            error_message = "Invaild email or password"
            return render(
                request, "car_lease_login.html", {"error_message": error_message}
            )
        try:
            user = Car_leaser.objects.get(car_owner_email=email)
            passw = Car_leaser.objects.get(
                car_owner_password=password, car_owner_email=email
            )
            if not passw:
                raise Car_leaser.DoesNotExist
        except Car_leaser.DoesNotExist:
            error_message = "Invalid email or password"
            return render(
                request, "car_lease_login.html", {"error_message": error_message}
            )
        return redirect("/car_lease_dashboard")
    else:
        return render(request, "car_lease_login.html")


def car_lease_signup(request):
    if request.method == "POST":
        try:
            email = request.POST["email"]
            phone_number = request.POST["phone-number"]
            username = request.POST["username"]
            print(username)
            password = request.POST["password"]
            print(password)
            confirm_password = request.POST["confirm-password"]
            car_company = request.POST["car-company"]
            car_model = request.POST["car-model"]
            price = request.POST["car-price"]
        except MultiValueDictKeyError:
            error_message = "Please fill all fields"
            return render(
                request, "car_lease_signup.html", {"error_message": error_message}
            )
        user = Car_leaser.objects.filter(
            car_owner_name=username,
            car_owner_mobile_number=phone_number,
            car_owner_password=password,
            car_owner_email=email,
            car_owner_car_company=car_company,
            car_owner_car_model=car_model,
            car_owner_car_price=price,
        )
        if user.exists():
            error_message1 = "Car renter already exists"
            print(error_message1)
            return render(
                request, "car_lease_signup.html", {"error_message": error_message1}
            )
        if confirm_password != password:
            error_message2 = "Password and Confirm password do not match"
            print(error_message2)
            return render(
                request, "car_lease_signup.html", {"error_message": error_message2}
            )
        user1 = Car_leaser(
            car_owner_name=username,
            car_owner_mobile_number=phone_number,
            car_owner_password=password,
            car_owner_email=email,
            car_owner_car_company=car_company,
            car_owner_car_model=car_model,
            car_owner_car_price=price,
        )
        user1.save()
        messages.success(request, "Your account has been created!")
        return redirect("/car_lease_login")
    return render(request, "car_lease_signup.html")


def car_lease_dashboard(request):
    return render(request, "car_lease_dashboard.html")
