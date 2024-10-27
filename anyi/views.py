from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
from django.contrib import messages
from .models import Role, Admin, Bursal, Teacher

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
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Check user role and redirect
                if Admin.objects.filter(user=user).exists():
                    return redirect('admin_dashboard')
                elif Bursal.objects.filter(user=user).exists():
                    return redirect('bursal_dashboard')
                elif Teacher.objects.filter(user=user).exists():
                    return redirect('teacher_dashboard')
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()

    return render(request, 'anyi/admin_login.html', {'form': form})


def student_dashboard(request):
    return render(request, 'anyi/login.html')

def bursal_dashboard(request):
    return render(request, 'anyi/bursal_dashboard.html')

def teacher_dashboard(request):
    return render(request, 'anyi/teacher_dashboard.html')

def admin_dashboard(request):
    return render(request, 'anyi/admin_dashboard.html')



def student_login(request):
    return render(request, 'anyi/login.html')

def bursal_login(request):
    return render(request, 'anyi/bursal_login.html')

def teacher_login(request):
    return render(request, 'anyi/teacher_login.html')


def enrol(request):
    
    return render(request, 'anyi/user_register.html')

def user_enrol(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            fname = form.cleaned_data['fname']
            sname = form.cleaned_data['sname']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            phonenum = form.cleaned_data['phonenum']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role'].role_name

            # Insert into the correct table based on role
            if role == 'Admin':
                Admin.objects.create(fname=fname, sname=sname, username=username,
                                     email=email, phonenum=phonenum, password=password)
            elif role == 'Bursal':
                Bursal.objects.create(fname=fname, sname=sname, username=username,
                                      email=email, phonenum=phonenum, password=password)
            elif role == 'Teacher':
                Teacher.objects.create(fname=fname, sname=sname, username=username,
                                       email=email, phonenum=phonenum, password=password)

            return redirect('admin_login')  # Redirect to some success page

    else:
        form = UserForm()

    return render(request, 'anyi/user_reg.html', {'form': form})

