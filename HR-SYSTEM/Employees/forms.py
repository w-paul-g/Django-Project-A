from django import forms
from Employees.models import Employee


# The Forms Start Here

class EmployeeForm(forms.ModelForm):
    fullname = forms.CharField(label="Name", widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 100%;', 'class': 'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'placeholder': 'Email', 'style': 'width: 100%;', 'class': 'form-control'}))
    emp_code = forms.CharField(label="Employee's Code", widget=forms.TextInput(attrs={'placeholder': "Employee's Code", 'style': 'width: 100%;', 'class': 'form-control'}))
    mobile_no = forms.CharField(label="Mobile No", widget=forms.TextInput(attrs={'placeholder': 'Mobile No', 'style': 'width: 100%;', 'class': 'form-control'}))
    position = forms.CharField(label="Position", widget=forms.TextInput(attrs={'placeholder': 'Position', 'style': 'width: 100%;', 'class': 'form-control'}))

    class Meta:
        model = Employee
        fields = ['fullname', 'email', 'emp_code', 'mobile_no', 'position']
