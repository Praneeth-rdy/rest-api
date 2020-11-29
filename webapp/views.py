from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer
from django.contrib.auth import authenticate


# Create your views here.
class EmployeeList(APIView):
    def get(self, request):
        try:
            auth = request.user.is_authenticated
        except:
            auth = False
        
        if auth:
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
        else:
            return Response([{}])
    
    def post(self):
        pass

class Login(APIView):
    def get(self, request):
        try:
            auth = request.user.is_authenticated
        except:
            auth = False
        if auth:
            data = [{"loggedin": True}]
        else:
            data = [{"loggedin": False}]
        return Response(data)
    
    def post(self, request):
        username = str(request.POST['email'])
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            try:
                id = request.GET.get('id')
                employee = Employee.objects.filter(id=id)[0]
            except:
                employee = None
            
            if employee:
                serializer = EmployeeSerializer(employee, many=False)
            else:
                employees = Employee.objects.all()
                serializer = EmployeeSerializer(employees, many=True)
            return Response(serializer.data)
        else:
            return Response([{}])