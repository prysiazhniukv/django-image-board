from django.urls import path, include
from . import views

app_name = "boards"

urlpatterns = [
    path("<slug:slug>/", views.book_details, name="board_details"),
    path("<slug:slug>/new/", views.thread_create, name="thread_create"),
]
