from datetime import date
from urllib import response
from django.shortcuts import render
from staff.models import *
from django.http import JsonResponse

# Function to render Homepage
# def home(request):
#     employee_list = Employee.objects.all()
#     return render(request, "home.html", {"employees":employee_list})
def home(request):
    return render(request, "home.html")

# Jason
def employee_jason(request):
    employees = Employee.objects.all()
    data = [employee.get_data() for employee in employees]
    response = {'data': data}
    return JsonResponse(response)