from django.shortcuts import render


# Create your views here.
def car_lease_login(request):
    return render(request, "car_lease_login.html")


def car_lease_signup(request):
    return render(request, "car_lease_signup.html")


def car_lease_dashboard(request):
    return render(request, "car_lease_dashboard.html")
