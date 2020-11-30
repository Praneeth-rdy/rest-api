from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from ..models import *
from .serializers import *


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
            blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass