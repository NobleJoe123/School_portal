from django.db import models
from django.utils import timezone

class Admin(models.Model):
    fname = models.CharField(max_length=100)
    sname = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=255, unique=True)
    phonenum = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    image = models.ImageField(upload_to='student_images/', blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Admin: {self.username}"


class Bursal(models.Model):
    fname = models.CharField(max_length=100)
    sname = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=255, unique=True)
    phonenum = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    image = models.ImageField(upload_to='student_images/', blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Bursal: {self.username}"
    





class Teacher(models.Model):
    # Personal Details
    fname = models.CharField(max_length=50, verbose_name="First Name")
    sname = models.CharField(max_length=50, verbose_name="Surname")
    mname = models.CharField(max_length=50, blank=True, null=True, verbose_name="Middle Name")
    age = models.PositiveIntegerField(verbose_name="Age")
    phone = models.CharField(max_length=15, verbose_name="Phone Number")
    sex = models.CharField(
        max_length=6,
        choices=[("Male", "Male"), ("Female", "Female")],
        verbose_name="Gender",
    )
    address = models.TextField(verbose_name="Address", null=True, blank=True)
    emergency = models.CharField(max_length=100, verbose_name="Emergency Contact")

    # File Uploads
    cv = models.FileField(upload_to="uploads/cv/", verbose_name="CV", blank=True, null=True)
    passport = models.ImageField(upload_to="uploads/passport/", verbose_name="Passport Image")

    # Academic Details
    CLASS_CHOICES = [
        ("JSS1", "JSS1"), ("JSS2", "JSS2"), ("JSS3", "JSS3"),
        ("SS1", "SS1"), ("SS2", "SS2"), ("SS3", "SS3"),
    ]
    class_teacher = models.CharField(max_length=5, choices=CLASS_CHOICES, verbose_name="Class Teacher")

    SUBJECT_CHOICES = [
        ("Mathematics", "Mathematics"),
        ("English Language", "English Language"),
        ("Nigerian Language", "Nigerian Language"),
        ("Basic Science", "Basic Science"),
        ("Social Studies", "Social Studies"),
        ("Fine Arts/Creative Art", "Fine Arts/Creative Art"),
        ("Agricultural Science", "Agricultural Science"),
        ("Civic Education", "Civic Education"),
        ("Christian Religion Studies", "Christian Religion Studies"),
        ("Physical and Health Education", "Physical and Health Education"),
        ("Business Studies", "Business Studies"),
        ("French", "French"),
        ("Computer Studies", "Computer Studies"),
        ("Home Economics", "Home Economics"),
        ("Basic Technology", "Basic Technology"),
        ("Biology", "Biology"),
        ("Physics", "Physics"),
        ("Chemistry", "Chemistry"),
        ("Further Mathematics", "Further Mathematics"),
        ("Technical Drawing", "Technical Drawing"),
        ("Food and Nutrition", "Food and Nutrition"),
        ("Accounting", "Accounting"),
        ("Commerce", "Commerce"),
        ("Book-keeping", "Book-keeping"),
        ("Data Processing", "Data Processing"),
        ("Economics", "Economics"),
        ("Government", "Government"),
        ("Literature – in- English", "Literature – in- English"),
        ("Christian Religion Knowledge", "Christian Religion Knowledge"),
        ("Fine Art/Creative Art", "Fine Art/Creative Art"),
        ("Geography", "Geography"),
    ]
    subject_teacher = models.CharField(max_length=50, choices=SUBJECT_CHOICES, verbose_name="Subject Teacher")

    # Login Details
    password = models.CharField(max_length=128, verbose_name="Password")

    def __str__(self):
        return f"{self.sname}, {self.fname}"

class Role(models.Model):
    role_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.role_name
    


class jss1(models.Model):
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phonenum = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    lga = models.CharField(max_length=100)
    dob = models.DateField()
    guardianname = models.CharField(max_length=100)
    image = models.ImageField(upload_to='student_images/', blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"jss1: {self.username}"
    

class jss2(models.Model):
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phonenum = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    lga = models.CharField(max_length=100)
    dob = models.DateField()
    guardianname = models.CharField(max_length=100)
    image = models.ImageField(upload_to='student_images/', blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"jss2: {self.username}"
    
class jss3(models.Model):
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phonenum = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    lga = models.CharField(max_length=100)
    dob = models.DateField()
    guardianname = models.CharField(max_length=100)
    image = models.ImageField(upload_to='student_images/', blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"jss3: {self.username}"
    
# class ss1(models.Model):
#     firstname = models.CharField(max_length=100)
#     surname = models.CharField(max_length=100)
#     middlename = models.CharField(max_length=100, blank=True, null=True)
#     username = models.CharField(max_length=100, unique=True)
#     email = models.EmailField(max_length=255, unique=True)
#     phonenum = models.CharField(max_length=15)
#     password = models.CharField(max_length=255)
#     state = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
#     lga = models.CharField(max_length=100)
#     dob = models.DateField()
#     guardianname = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='student_images/', blank=True, null=True)
#     datetime = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"ss1: {self.username}"
    
class ss1(models.Model):
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phonenum = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    lga = models.CharField(max_length=100)
    dob = models.DateField()
    guardianname = models.CharField(max_length=100)
    image = models.ImageField(upload_to='student_images/', blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ss1: {self.username}"
    
class ss2(models.Model):
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phonenum = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    lga = models.CharField(max_length=100)
    dob = models.DateField()
    guardianname = models.CharField(max_length=100)
    image = models.ImageField(upload_to='student_images/', blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ss2: {self.username}"
    

class ss3(models.Model):
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phonenum = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    lga = models.CharField(max_length=100)
    dob = models.DateField()
    guardianname = models.CharField(max_length=100)
    image = models.ImageField(upload_to='student_images/', blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ss3: {self.username}"


