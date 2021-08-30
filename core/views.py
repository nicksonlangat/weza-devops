from .serializers import EmployeeSerializer
from .models import Employee
from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

class EmployeeViewset(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
