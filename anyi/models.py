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
    fname = models.CharField(max_length=50, verbose_name="First Name",  null=True, blank=True)
    sname = models.CharField(max_length=50, verbose_name="Surname",  null=True, blank=True)
    mname = models.CharField(max_length=50, blank=True, null=True, verbose_name="Middle Name")
    username = models.CharField(max_length=50, blank=True, null=True, verbose_name="Username")
    dob = models.DateField(verbose_name="Dob",  null=True, blank=True)
    phone = models.CharField(max_length=15, verbose_name="Phone Number", default="+234",  null=True, blank=True)
    sex = models.CharField(
        max_length=6,
        choices=[("Male", "Male"), ("Female", "Female")],
        verbose_name="Gender",  null=True, blank=True
    )
    address = models.TextField(verbose_name="Address", null=True, blank=True)
    emergency = models.CharField(max_length=100, verbose_name="Emergency Contact",  null=True, blank=True)

    # File Uploads
    cv = models.FileField(upload_to="uploads/cv/", verbose_name="CV", blank=True, null=True)
    passport = models.ImageField(upload_to="uploads/passport/", verbose_name="Passport Image",  null=True, blank=True)

    # Academic Details
    CLASS_CHOICES = [
        ("JSS1", "JSS1"), ("JSS2", "JSS2"), ("JSS3", "JSS3"),
        ("SS1", "SS1"), ("SS2", "SS2"), ("SS3", "SS3"),
    ]
    class_teacher = models.CharField(max_length=5, choices=CLASS_CHOICES, verbose_name="Class Teacher",  null=True, blank=True)

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
        ("Marketing", "Marketing"),
        ("Data Processing", "Data Processing"),
        ("Economics", "Economics"),
        ("Government", "Government"),
        ("Literature – in- English", "Literature – in- English"),
        ("Christian Religion Knowledge", "Christian Religion Knowledge"),
        ("Islamic Religion Knowledge", "Islamic Religion Knowledge"),
        ("Geography", "Geography"),
    ]
    subject_teacher = models.CharField(max_length=50, choices=SUBJECT_CHOICES, verbose_name="Subject Teacher",  null=True, blank=True)

    # Login Details
    password = models.CharField(max_length=128, verbose_name="Password",  null=True, blank=True)

    def __str__(self):
        return f"{self.sname}, {self.fname}"

class Role(models.Model):
    role_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.role_name



class Student(models.Model):
    CLASS_CHOICES = [
        ("JSS1", "JSS1"),
        ("JSS2", "JSS2"),
        ("JSS3", "JSS3"),
        ("SS1", "SS1"),
        ("SS2", "SS2"),
        ("SS3", "SS3"),
    ]

    DEPARTMENT_CHOICES = [
        ("Science", "Science"),
        ("Commercial", "Commercial"),
        ("Art", "Art"),
    ]

    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phonenum = models.CharField(max_length=15)
    mobilenum = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    lga = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.TextField()
    guardianname = models.CharField(max_length=100)
    passport = models.ImageField(upload_to='student_images/', blank=True, null=True)
    student_class = models.CharField(max_length=5, choices=CLASS_CHOICES)
    department = models.CharField(max_length=15, choices=DEPARTMENT_CHOICES)
    adminum = models.CharField(max_length=20, unique=True, blank=True, editable=False)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lname}, {self.fname} ({self.student_class})"


class JSS1(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="jss1_student")

    def __str__(self):
        return f"JSS1: {self.student}"


class JSS2(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="jss2_student")

    def __str__(self):
        return f"JSS2: {self.student}"


class JSS3(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="jss3_student")

    def __str__(self):
        return f"JSS3: {self.student}"


class SS1(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="ss1_student")

    def __str__(self):
        return f"SS1: {self.student}"


class SS2(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="ss2_student")

    def __str__(self):
        return f"SS2: {self.student}"


class SS3(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="ss3_student")

    def __str__(self):
        return f"SS3: {self.student}"


class Science(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="science_student")

    def __str__(self):
        return f"Science: {self.student}"


class Commercial(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="commercial_student")

    def __str__(self):
        return f"Commercial: {self.student}"


class Art(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="art_student")

    def __str__(self):
        return f"Art: {self.student}"
    


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    week = models.IntegerField()
    term = models.IntegerField()
    is_present = models.BooleanField(default=False)

    class Meta:
        unique_together = ('student', 'week', 'term')

    def __str__(self):
        return f"Student: {self.student}, Term: {self.term}, Week: {self.week}, Present: {self.is_present}"

    
    
    
    
class TestScore(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    test_score = models.IntegerField()
    exam_score = models.IntegerField()




