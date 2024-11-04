from django.contrib import admin
from .models import * 

@admin.register(Employee)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email_id', 'phone_number', 'employee_gender', 'date_of_birth', 'age']

@admin.register(Departments)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["department_name"]
