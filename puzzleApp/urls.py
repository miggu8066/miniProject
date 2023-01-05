

from django.urls import path
from puzzleApp import views

app_name = "puzzleApp"
urlpatterns = [
    path("name/", views.name),
    path("start/", views.start),
    path("insert/", views.insert),
    path("show/", views.show, name='show'),

    path("test/", views.test),
]