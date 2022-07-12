from django.shortcuts import render
from staff.models import *

# Function to render Homepage
def home(request):
    employee_list = Employee.objects.all()
    return render(request, "home.html", {"employees":employee_list})