from django.shortcuts import render, redirect
from django.contrib import messages
from Employees.forms import EmployeeForm


# Create your views here.
def employee_form(request):
    if request.method == 'GET':
        form = EmployeeForm()
        return render(request, 'employee_form.html', {'form': form})
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_form')


def employee_list(request):
    return render(request, 'employee_list.html')
