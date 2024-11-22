from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm, StudentForm
from django.contrib import messages
from .models import Role, Admin, Bursal, Teacher, Student

# Create your views here.



def home (request):
    return render(request, 'anyi/index.html')

def about (request):
    return render(request, 'anyi/about.html')

def courses (request):
    return render(request, 'anyi/courses.html')
    
def admin_register(request):
    return render(request, 'anyi/admin_register.html')

def teacher_board(request):
    return render(request, 'bursal_dashboard.html')


# login session

def admin_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Check if user is in Admin table
            admin_user = Admin.objects.filter(username=username, password=password).first()
            if admin_user:
                # Authenticate and log in admin user
                request.session['role'] = 'Admin'  # Store role in session
                request.session['user_id'] = admin_user.id  # Store user ID for later use
                return redirect('admin_dashboard')  # Redirect to admin dashboard
            
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
        
    return render(request, 'anyi/admin_login.html', {'form': form})


def student_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            student_models = [jss1, jss2, jss3, ss1, ss2, ss3]
            student = None

            for model in student_models:
                try:
                    student = model.objects.get(username=username)
                    if student.password == password:  # Simple password check
                        request.session['user_id'] = student.id
                        request.session['role'] = model.__name__.lower()  # Store model name as role
                        messages.success(request, 'Logged in successfully!')
                        return redirect('student_dashboard')  # Redirect based on role
                    else:
                        messages.error(request, 'Invalid password!')
                        return render(request, 'members/login.html', {'form': form})
                except model.DoesNotExist:
                    continue  # Move to the next model if the username isn't found

            # If we reach here, the user was not found in any model
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(request, 'anyi/login.html', {'form': form})



def bursal_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            bursal_user = Bursal.objects.filter(username=username, password=password).first()
            if bursal_user:
                request.session['role'] = 'Bursal'
                request.session['user_id'] = bursal_user.id
                return redirect('bursal_dashboard')  # Redirect to bursal dashboard
            
            
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
        
    return render(request, 'anyi/bursal_login.html', {'form':form})
        
def teacher_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)  # Use the LoginForm for authentication
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Fetch the teacher by username and check the password
            teacher_user = Teacher.objects.filter(phone=username).first()
            if teacher_user and teacher_user.password == password:  # Replace with hashed password check if necessary
                # Store the teacher's role and ID in the session
                request.session['role'] = 'Teacher'
                request.session['user_id'] = teacher_user.id
                messages.success(request, 'Login successful!')
                return redirect('teacher_dashboard')  # Redirect to the teacher's dashboard
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()  # Render an empty login form for GET requests
        
    return render(request, 'anyi/teacher_login.html', {'form': form})


# login ends



# enrol form
def enrol(request):
    return render(request, 'anyi/enrol.html')



def add_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("success")  # Replace with your success page
    else:
        form = TeacherForm()
    return render(request, "anyi/add_teacher.html", {"form": form})


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Replace with your actual redirect
    else:
        form = StudentForm()

    return render(request, 'anyi/add_student.html', {'form': form})


# DASHBOARDS STARTS


def student_dashboard(request):
    user_id = request.session.get('user_id')
    
    if not user_id:
        return redirect('student_login')
    
    student = None
    for model in [jss1, jss2, jss3, ss1, ss2, ss3]:
        try:
            student = model.objects.get(id=user_id)
            break
        except model.DoesNotExist:
            continue

    if not student:
        messages.error(request, "Student not found.")
        return redirect('student_login')

    return render(request, 'anyi/student_dashboard.html', {
        'firstname': student.firstname ,
        'surname': student.surname,
        'image_url': student.image.url if student.image else None
        })


def bursal_dashboard(request):

    user_id = request.session.get('user_id')
    
    if not user_id:
        return redirect('bursal_login')
    
    
    bursal = None
    for model in [Bursal]:
        try:
            bursal = model.objects.get(id=user_id)
            break
        except model.DoesNotExist:
            continue

    if not bursal:
        messages.error(request, "Teacher not found.")
        return redirect('bursal_login')

    data = Bursal.objects.all()[:10]  


    return render(request, 'anyi/bursal_dashboard.html', 
                  {'data':data,
                   'firstname': data.firstname ,
                    'surname': data.surname,
                    'image_url': data.image.url if data.image else None})


def teacher_dashboard(request):

    user_id = request.session.get('user_id')
    
    if not user_id:
        return redirect('teacher_login')
    
    teacher = None
    for model in [Teacher]:
        try:
            teacher = model.objects.get(id=user_id)
            break
        except model.DoesNotExist:
            continue

    if not teacher:
        messages.error(request, "Teacher not found.")
        return redirect('teacher_login')
    

    # teacher_user_id = teacher.user_id  # Assuming Teacher model has `class_id`
    # students = ss3.objects.filter(user_id=teacher_user_id)

    students = ss3.objects.all()  # Or filter as needed

    weeks = range(1, 15)
    check = range(5)
    
    context = {
        "data": students,
        "weeks": weeks,  # Pass the weeks range to the template
        "check": check,
        'firstname': teacher.fname ,
        'surname': teacher.sname,
        'image_url': teacher.passport.url if teacher.passport else None 
    }


    return render(request, 'anyi/teacher_dashboard.html', context)


def admin_dashboard(request):
    user_id = request.session.get('user_id')
    
    if not user_id:
        return redirect('admin_login')
    
    
    admin = None
    for model in [Admin]:
        try:
            admin = model.objects.get(id=user_id)
            break
        except model.DoesNotExist:
            continue

    if not admin:
        messages.error(request, "Admin not found.")
        return redirect('admin_login')

    people = Admin.objects.all()[:10]
    # if not Admin.objects.filter(user=request.user).exists():
    #     return redirect('admin_login')
    return render(request, 'anyi/admin_dashboard.html', 
                  {'people': people,
                   'firstname': admin.fname ,
                   'surname': admin.sname,
                   'image_url': admin.image.url if admin.image else None})

# DASHBOARDS ENDS

# views.py


def admin_enrol(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            # Extract data from the form
            fname = form.cleaned_data['fname']
            sname = form.cleaned_data['sname']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            phonenum = form.cleaned_data['phonenum']
            password = form.cleaned_data['password']
            image = form.cleaned_data['image']
            role = form.cleaned_data['role'].role_name

            # Insert into the correct table based on role
            if role == 'Admin':
                Admin.objects.create(
                    fname=fname, sname=sname, username=username,
                    email=email, phonenum=phonenum, password=password, image=image
                )
            elif role == 'Bursal':
                Bursal.objects.create(
                    fname=fname, sname=sname, username=username,
                    email=email, phonenum=phonenum, password=password, image=image
                )
            elif role == 'Teacher':
                Teacher.objects.create(
                    fname=fname, sname=sname, username=username,
                    email=email, phonenum=phonenum, password=password, image=image
                )

            messages.success(request, 'User registered successfully!')
            return redirect('admin_login')  # Redirect to login or success page

    else:
        form = UserForm()

    return render(request, 'anyi/admin_reg.html', {'form': form})


# def custom_404_view(request, exception):
#     return render(request, 'anyi/404.html', status=404)

def student_register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save data to the appropriate model
            return redirect('student_login')  # Redirect to a success page or any other view
    else:
        form = StudentForm()

    return render(request, 'anyi/student_register.html', {'form': form})