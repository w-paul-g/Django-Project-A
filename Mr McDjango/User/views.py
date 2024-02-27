from django.shortcuts import render
from .forms import RegisterForm, RegistrationForm


# Create your views here.

def index(request):
    return render(request, 'index.html')


def signup(request):
    form = RegistrationForm
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})


def login(request):
    return render(request, 'login.html')


def logout(request):
    return render(request, 'logout.html')


def signin(request):
    form = RegisterForm()
    return render(request, 'signin.html', {'form': form})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def gallery(request):
    return render(request, 'gallery.html')
