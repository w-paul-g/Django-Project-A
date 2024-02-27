from django.shortcuts import render
from 

# Create your views here.
def index(request):
    return render(request, 'index.html')


def signin(request):
    form = StudentForm()
    return render(request, 'signin.html')


def activation(request):
    return render(request, 'activation.html')
