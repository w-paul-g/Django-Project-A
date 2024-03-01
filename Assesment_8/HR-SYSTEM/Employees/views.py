from django.shortcuts import render, redirect
from django.contrib import messages
from Employees.forms import Employee_Form, Next_of_kin_Form


# Create your views here.
def employee_form(request):
    if request.method == 'GET':
        form = Employee_Form()
        messages.warning(request, "You have already registered")
        return render(request, 'employee_form.html', {'form': form})
    else:
        form = Employee_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have registered successfully")
            return redirect('employee_form')


def next_of_kin_form(request):
    if request.method == 'GET':
        form = Next_of_kin_Form()
        messages.warning(request, "You have already registered")
        return render(request, 'next_of_kin_form.html', {'form': form})
    else:
        form = Next_of_kin_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have registered successfully")
            return redirect('next_of_kin_form')
