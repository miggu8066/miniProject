from django.urls import path
from puzzleApp import views

app_name = "puzzleApp"
urlpatterns = [
    path("name/", views.name),
    path("", views.start),
    path("insert/", views.insert),
    path("rank/", views.rank, name='rank'),
    path("fileupload/", views.fileUpload, name='fileupload'),
    path("fileupload1/", views.fileUpload1, name='fileupload1'),
    path("file/", views.file, name='file'),
]