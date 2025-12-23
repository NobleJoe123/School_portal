from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm, StudentForm, TeacherForm
from django.contrib import messages
from .models import Role, Admin, Bursal, Teacher, Student, Attendance, TestScore
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.



def home (request):
    return render(request, 'anyi/index.html')

def about (request):
    return render(request, 'anyi/about.html')

def courses (request):
    return render(request, 'anyi/courses.html')
    
def admin_register(request):
    return render(request, 'anyi/admin_register.html')

# def teacher_board(request):
#     return render(request, 'bursal_dashboard.html')


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
            teacher_user = Teacher.objects.filter(username=username).first()
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
            return redirect("teacher_login")  # Replace with your success page
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
    
    teacher_id = request.session.get('user_id')
    if not teacher_id:
        return redirect('teacher_login')
    
    teacher = Teacher.objects.get(id=teacher_id)


    ss1_students = Student.objects.none()
    ss2_students = Student.objects.none()
    ss3_students = Student.objects.none()
    jss1_students = Student.objects.none()
    jss2_students = Student.objects.none()
    jss3_students = Student.objects.none()


    # ss1_students = Student.objects.filter(student_class="SS1", department__contains=teacher.subject_teacher)
    # ss2_students = Student.objects.filter(student_class="SS2", department__contains=teacher.subject_teacher)
    # ss3_students = Student.objects.filter(student_class="SS3", department__contains=teacher.subject_teacher)



    # Initialize empty QuerySets
    subject_students = Student.objects.none()
    class_students = Student.objects.none()

    weeks = range(1, 15)
    check = range(1, 6)
    term = 1

    class_students = Student.objects.filter(student_class=teacher.class_teacher) if teacher.class_teacher else Student.objects.none()

    # Attendance data
    attendance_data = {}
    if class_students.exists():
        for attendance in Attendance.objects.filter(student__in=class_students, term=term):
            key = f"term{attendance.term}_{attendance.student.id}_week{attendance.week}"
            attendance_data[key] = attendance.is_present

      # Current term# Example: Filter students

    # Fetch attendance data


    # Mapping subjects to departments and classes
    science_subjects = [
        "Mathematics", "English Language", "Civic Education", "Computer Studies",
        "Biology", "Physics", "Chemistry", "Further Mathematics",
        "Technical Drawing", "Economics", "Geography", "Data Processing", "Marketing",
    ]
    art_subjects = [
        "Mathematics", "English Language", "Civic Education", "Computer Studies",
        "Literature – in- English", "Government", "History", "Islamic Religion Knowledge",
        "Christian Religion Knowledge", "Data Processing", "Marketing", "Book-keeping", "Economics",
    ]
    commercial_subjects = [
        "Mathematics", "English Language", "Civic Education", "Computer Studies",
        "Accounting", "Commerce", "Marketing", "Economics", "Book-keeping",
    ]
    junior_subjects = [
        "Mathematics", "English Language", "Civic Education", "Computer Studies",
        "Basic Science", "Social Studies", "Fine Arts/Creative Art", "Agricultural Science",
        "Christian Religion Studies", "Physical and Health Education", "Business Studies",
        "French", "Home Economics", "Basic Technology", "Nigerian Language",
    ]

    # Filter students based on teacher's subject
    if teacher.subject_teacher:
        if teacher.subject_teacher in science_subjects:
            subject_students = Student.objects.filter(department="Science")
        elif teacher.subject_teacher in art_subjects:
            subject_students = Student.objects.filter(department="Art")
        elif teacher.subject_teacher in commercial_subjects:
            subject_students = Student.objects.filter(department="Commercial")
        elif teacher.subject_teacher in junior_subjects:
            # Assuming teacher's `class_teacher` indicates specific junior classes
            if teacher.class_teacher in ["JSS1", "JSS2", "JSS3"]:
                subject_students = Student.objects.filter(student_class=teacher.class_teacher)

    # Filter students in the teacher's assigned class
    if teacher.class_teacher:
        class_students = Student.objects.filter(student_class=teacher.class_teacher)

    if teacher.subject_teacher in science_subjects:
        ss1_students = Student.objects.filter(student_class="SS1", department="Science")
        ss2_students = Student.objects.filter(student_class="SS2", department="Science")
        ss3_students = Student.objects.filter(student_class="SS3", department="Science")
    elif teacher.subject_teacher in art_subjects:
        ss1_students = Student.objects.filter(student_class="SS1", department="Art")
        ss2_students = Student.objects.filter(student_class="SS2", department="Art")
        ss3_students = Student.objects.filter(student_class="SS3", department="Art")
    elif teacher.subject_teacher in commercial_subjects:
        ss1_students = Student.objects.filter(student_class="SS1", department="Commercial")
        ss2_students = Student.objects.filter(student_class="SS2", department="Commercial")
        ss3_students = Student.objects.filter(student_class="SS3", department="Commercial")
    elif teacher.subject_teacher in junior_subjects:
        jss1_students = Student.objects.filter(student_class="JSS1")
        jss2_students = Student.objects.filter(student_class="JSS2")
        jss3_students = Student.objects.filter(student_class="JSS3")


    class_names = ["JSS1", "JSS2", "JSS3", "SS1", "SS2", "SS3"]

    students_by_class = [
        {
            "class_name": class_name,
            "students": Student.objects.filter(student_class=class_name),
        }
        for class_name in class_names
    ]

    classes = {
        'JSS1': jss1_students,
        'JSS2': jss2_students,
        'JSS3': jss3_students,
        'SS1': ss1_students,
        'SS2': ss2_students,
        'SS3': ss3_students,
        }
      

    # Render the dashboard with relevant students
    context = {
        'teacher': teacher,
        'ss1_students': ss1_students,
        'ss2_students': ss2_students,
        'ss3_students': ss3_students,
        'jss1_students': jss1_students,
        'jss2_students': jss2_students,
        'jss3_students': jss3_students, 
        'subject_students': subject_students,
        "students_by_class": students_by_class,
        'classes': classes,
        'attendance_data' : attendance_data,
        'class_students': class_students,
        'weeks' : weeks,
        'check' : check,
        'image_url' : teacher.passport.url if teacher.passport else None,
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



# Atendance and score #

@csrf_exempt
def save_attendance(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            for entry in data:
                student_id = entry['student_id']
                week = entry['week']
                present = entry['present']

                # Save attendance
                Attendance.objects.update_or_create(
                    student_id=student_id, term=1, week=week, defaults={'present': present}
                )
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})

# def get_data(request, class_name):
#     students = Student.objects.filter(class_name=class_name)
#     attendance = Attendance.objects.filter(student__class_name=class_name)
#     test_scores = TestScore.objects.filter(student__class_name=class_name)

#     response = {
#         "students": list(students.values()),
#         "attendance": list(attendance.values()),
#         "test_scores": list(test_scores.values())
#     }
#     return JsonResponse(response)

# def save_data(request):
#     if request.method == "POST":
#         # Parse and save attendance or test score data
#         data = request.POST.get("data")
#         # Save to database
#         return JsonResponse({"success": True})