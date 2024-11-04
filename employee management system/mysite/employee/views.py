from types import NoneType
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import *
import django.http as http

def home(request):
    employees = Employee.objects.all()  
    return render(request, 'home.html', {'employees': employees})
  
def employee(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)
        
        
        if employee.date_of_birth:
            today = datetime.today()
            age = today.year - employee.date_of_birth.year - ((today.month, today.day) < (employee.date_of_birth.month, employee.date_of_birth.day))
        else:
            age = None
            
    except Employee.DoesNotExist:
        employee = None
        age = None

    return render(request, 'employee.html', {'employee': employee, 'age': age})





    


