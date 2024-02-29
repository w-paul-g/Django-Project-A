from django import forms
from Employees.models import Employee


# The Forms Start Here

class EmployeeForm(forms.ModelForm):
    fullname = forms.CharField(label="Name")
    email = forms.EmailField(label="Email")
    emp_code = forms.CharField(label="Employee's Code")
    mobile_no = forms.CharField(label="Mobile No")
    position = forms.CharField(label="Position")

    class Meta:
        model = Employee
        fields = ['fullname', 'email', 'emp_code', 'mobile_no', 'position']
