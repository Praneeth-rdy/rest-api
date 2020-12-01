from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from ..models import *
from .serializers import *
from django.contrib.auth import authenticate, login, logout


# Create your views here.
class Employees(APIView):
    def get(self, request):
        try:
            id = request.GET.get('id')
            employee = Employee.objects.filter(id=id)[0]
        except:
            employee = None
        employees = Employee.objects.all()
        if employee:
            serializer = EmployeeSerializer(employee, many=False)
        else:
            serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass

class Blogs(APIView):
    def get(self, request):
        try:
            req_title = request.GET.get('title')
            blogs = Blog.objects.filter(title=req_title)
        except:
            pass
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        key = request.POST.get('key')
        if key == '1202':
            blogs = Blog.objects.all()
            serializer = BlogSerializer(blogs, many=True)
            return Response(serializer.data)
        else:
            data = [{"response": "Key is wrong or not found"}]
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            print(request.user)
            #logout(request)
            return redirect("/webapp/blogs/")
        else:
            data = [{"response": "Login First"}]
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        print('\n\n\n\n', username, password, '\n\n\n\n')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/webapp/blogs/")
        else:
            user = CustomUser.objects.get(username=username)
            if password != user.password:
                data = [{"response": "Invalid password"}]
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
class Logout(APIView):
    def get(self, request):
        logout(request)
