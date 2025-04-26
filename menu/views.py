from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "menu/index.html")


def about(request):
    return HttpResponse("This is the About page.")


def services(request):
    return HttpResponse("This is the Services page.")


def web_dev(request):
    return HttpResponse("This is the Web Development page.")
