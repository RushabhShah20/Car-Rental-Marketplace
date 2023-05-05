from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# from .serializers import UserSerializer


# Create your views here.
def index(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")


def about():
    print()


@api_view(["POST"])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"user_id": serializer.instance.id}, status=201)
    else:
        return Response(serializer.errors, status=400)
