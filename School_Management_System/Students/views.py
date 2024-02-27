from django.shortcuts import render

from Students.forms import StudentForm, StudentComplains


# Create your views here.
def index(request):
    return render(request, 'index.html')


def signup(request):
    form = StudentForm()
    return render(request, 'signup.html', {'form': form})


def activation(request):
    return render(request, 'activation.html')


def register(request):
    form = StudentComplains()
    return render(request, 'register.html', {'form': form})
