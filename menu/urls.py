from django.http import HttpResponse
from django.urls import path

from menu import views
from menu.apps import MenuConfig

app_name = MenuConfig.name

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("services/web-dev/", views.web_dev, name="web_dev"),
    # Добавьте остальные маршруты
]
