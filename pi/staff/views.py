from datetime import date
from email import message
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
def add_employee(request):
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
            employee.gender = request.POST.get('gender')
            employee.note = request.POST.get('note')
            employee.save()
            messages.success(request, "Employee added successfully !!")
            return HttpResponseRedirect("/")
        else:
            return render(request, 'add.html')

# Function to view employee data individually
def employee(request, employee_id):
    employee = Employee.objects.get(id = employee_id)
    if employee != None:
        return render(request, "edit.html", {'employee:employee'})

# Function to edit employee
def edit_employee(request):
    if request.method == "POST":
        employee = Employee.objects.get(id = request.POST.get('id'))
        if employee != None:
            employee.name = request.POST.get('name')
            employee.email = request.POST.get('email')
            employee.occupation = request.POST.get('occupation')
            employee.salary = request.POST.get('salary')
            employee.gender = request.POST.get('gender')
            employee.note = request.POST.get('note')
            employee.save()
            messages.success(request, "Employee update successfully !!")
            return HttpResponseRedirect("/")

# Function to delete Employee
def delete_employee(request, employee_id) :
    employee = Employee.objects.get(id = employee_id)
    employee.delete()
    message.success(request, "Employee delete successfully !!")  
    return HttpResponseRedirect("/")  

