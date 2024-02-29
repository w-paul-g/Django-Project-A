from django.shortcuts import render, redirect

from Students.forms import StudentForm, StudentComplains, AdmissionForm

from django.contrib import messages


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


def admission(request):
    form = AdmissionForm
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            form.save()
            form = AdmissionForm
            messages.success(request, 'Welcome')
            return redirect('index')
    return render(request, 'admission.html', {'form': form})

