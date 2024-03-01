from django import forms

from Employees.models import Employee_Detail, Next_of_kin_Detail


# 1 Employee Detail Form
class Employee_Form(forms.ModelForm):
    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    phone_no = forms.CharField(label="Phone No", required=True)
    password = forms.PasswordInput()

    class Meta:
        model = Employee_Detail
        fields = ['first_name', 'last_name', 'phone_no', 'password']


class Next_of_kin_Form(forms.ModelForm):
    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    employee_name = forms.CharField(label="Employee Name", required=True)
    phone_no = forms.CharField(label="Phone No", required=True)
    ID_No = forms.NumberInput()

    class Meta:
        model = Next_of_kin_Detail
        fields = ['first_name', 'last_name', 'employee_name', 'ID_No', 'phone_no']
