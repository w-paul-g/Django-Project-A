from django import forms
from Students.models import Contact


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
