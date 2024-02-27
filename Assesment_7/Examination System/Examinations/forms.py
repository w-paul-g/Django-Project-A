from django import forms


class StudentForm(forms.Form):
    name = forms.CharField(label='Enter your Name', max_length=100, required=True)
    age = forms.IntegerField(min_value=0, label='Enter your age', required=True)
    email = forms.EmailField(label='Enter your email', required=True)
    check = forms.BooleanField(label='Joining the institution means that you agree to its rules and regulations.', required='True')
    category = forms.CharField(Choices=[('Student', 'Student'), ('Parent', 'Parent'), ('Teacher', 'Teacher')])
