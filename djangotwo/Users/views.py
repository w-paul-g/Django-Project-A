from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'Index.html')


def aboutus(request):
    return render(request, 'AboutUs.html')


def contact(request):
    return render(request, 'Contacts.html')


def login(request):
    return render(request, 'Login.html')


def signup(request):
    return render(request, 'Register.html')
