from django import forms
from Students.models import Contact, StudentDetail


class StudentForm(forms.Form):
    name = forms.CharField(label='Enter your Name', max_length=100, required=True)
    age = forms.IntegerField(min_value=18, label='Enter your age', required=True)
    check = forms.BooleanField(label='Joining the institution means that you agree to its rules and regulations.',
                               required='True')
    category = forms.ChoiceField(choices=[('Student', 'Student'), ('Parent', 'Parent'), ('Teacher', 'Teacher')])


class StudentComplains(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']


class AdmissionForm(forms.ModelForm):
    # surname = forms.CharField(label='Enter your Surname')
    first_name = forms.CharField(label='Enter your First Name')
    last_name = forms.CharField(label='Enter your Last Name')
    age = forms.NumberInput()
    date_of_birth = forms.DateInput()

    class Meta:
        model = StudentDetail
        fields = ['first_name', 'last_name', 'age', 'date_of_birth']

