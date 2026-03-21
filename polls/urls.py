from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]

these are our changes