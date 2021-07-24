from django.shortcuts import render

# Create your views here.

from .models import Employee
from .serialization import EmployeeSer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class EmployeeTable(APIView):
    def get(self,req):
        obj=Employee.objects.all()
        sobj=EmployeeSer(obj,many=True)
        return Response(sobj.data)
