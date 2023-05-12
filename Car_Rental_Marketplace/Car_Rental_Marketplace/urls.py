"""car_rental_marketplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from car_rental import views
from car_lease import views as vs

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("signup/", views.signup, name="signup"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("car_lease_login/", vs.car_lease_login, name="car_lease_login"),
    path("car_lease_signup/", vs.car_lease_signup, name="car_lease_signup"),
    path("car_lease_dashboard/", vs.car_lease_dashboard, name="car_lease_dsahboard"),
]
