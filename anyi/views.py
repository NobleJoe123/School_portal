from django.shortcuts import render, redirect
from .forms import AdminRegistrationForm
from django.contrib import messages

# Create your views here.



def home (request):
    return render(request, 'anyi/index.html')

def about (request):
    return render(request, 'anyi/about.html')

def courses (request):
    return render(request, 'anyi/courses.html')
    
def admin_register(request):
    return render(request, 'anyi/admin_register.html')

def admin_login(request):
    return render(request, 'anyi/admin_login.html')

def student_login(request):
    return render(request, 'anyi/login.html')

def bursal_login(request):
    return render(request, 'anyi/bursal_login.html')

def teacher_login(request):
    return render(request, 'anyi/teacher_login.html')


def enrol(request):
    return render(request, 'anyi/user_register.html')

