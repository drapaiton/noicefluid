from django.urls import path
from . import views

from django.shortcuts import redirect

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', lambda request: redirect("https://drapaiton.github.io/"), name='about'),
]
