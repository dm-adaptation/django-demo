from django.http import HttpResponse
from django.shortcuts import render
from .services import fun_get_users

# Create your views here.


def index(request):
    fun_get_users()

    return HttpResponse("Hello, DM Database")
