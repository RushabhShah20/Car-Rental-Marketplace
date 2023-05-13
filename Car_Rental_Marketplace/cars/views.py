from django.shortcuts import render
from .models import Car


# Create your views here.
def car_detail(request):
    # user = Car.objects.filter(car_company="Tata")
    # print(user)
    # Car_company = user.car_company
    # print(car_company)
    # car_model = Car.car_model
    # date_of_registration = Car.date_of_registration
    # car_price = Car.car_price
    # car_registration_state = Car.car_registration_state
    # car_fueltype = Car.car_fueltype
    return render(request, "car_detail.html")
