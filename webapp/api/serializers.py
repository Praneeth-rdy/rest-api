from rest_framework import serializers
from ..models import *

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        #fields = ('firstname', 'lastname')
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        #fields = ('firstname', 'lastname')
        fields = '__all__'
