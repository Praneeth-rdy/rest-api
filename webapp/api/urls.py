from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'webapp'

urlpatterns = [
    path('employees/', views.Employees.as_view()),
    path('blogs/', views.Blogs.as_view()),
]