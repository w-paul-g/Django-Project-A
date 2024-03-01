from django.contrib import admin

from Employees.models import Employee_Detail, Next_of_kin_Detail

# Register your models here.
admin.site.register(Employee_Detail)
admin.site.register(Next_of_kin_Detail)
