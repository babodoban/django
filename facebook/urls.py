from django.urls import path
from facebook import views

urlpatterns = [
    path("", views.home, name="home"),
]