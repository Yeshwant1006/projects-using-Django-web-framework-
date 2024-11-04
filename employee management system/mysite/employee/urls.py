from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name = "home" ),
    path('employee/<int:employee_id>/', views.employee, name="employee"),
]
