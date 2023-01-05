from django.urls import path
from shootingApp import views

app_name = "shootingApp"
urlpatterns = [
    path("", views.main),
    path("insert/", views.insert),
    path("show/", views.show),
]