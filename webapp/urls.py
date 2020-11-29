from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'webapp'

urlpatterns = [
    path('employees/', views.EmployeeList.as_view()),
    path('login/', views.Login.as_view()),
]