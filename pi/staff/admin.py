from django.contrib import admin
from staff.models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'occupation', 'gender', 'created_at']
    search_fields = ['name', 'email', 'occupation']
    list_filter = ['gender']
    list_per_page = 8

admin.site.register(Employee, EmployeeAdmin)
