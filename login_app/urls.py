from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('create', views.create_new_user),
    path('login', views.login)
]