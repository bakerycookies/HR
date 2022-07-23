from datetime import date
from pyclbr import Function
from urllib import response
from django.shortcuts import render
from staff.models import *
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib import messages

# Function to render Homepage
def home(request):
    employee_list = Employee.objects.all()
    return render(request, "home.html", {"employees":employee_list})
# def home(request):
#     return render(request, "home.html")

# Jason
def employee_jason(request):
    employees = Employee.objects.all()
    data = [employee.get_data() for employee in employees]
    response = {'data': data}
    return JsonResponse(response)

# Function to render the page with all produts
def home(request):
    if request.method=="POST":
        if request.POST.get('name') \
            and request.POST.get('email') \
            and request.POST.get('occupation') \
            and request.POST.get('salary') \
            and request.POST.get('gender') \
            or request.POST.get('note'):
            employee = Employee()
            employee.name = request.POST.get('name')
            employee.email = request.POST.get('email')
            employee.occupation = request.POST.get('occupation')
            employee.salary = request.POST.get('salary')
            employee.note = request.POST.get('note')
