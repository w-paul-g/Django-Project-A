from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def signin(request):
    return render(request, 'signin.html')


def activation(request):
    return render(request, 'activation.html')
