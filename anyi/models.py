from django.db import models
from django.utils import timezone

class Admin(models.Model):
    fname = models.CharField(max_length=100)
    sname = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=255, unique=True)
    phonenum = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
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
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Bursal: {self.username}"


class Teacher(models.Model):
    fname = models.CharField(max_length=100)
    sname = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=255, unique=True)
    phonenum = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Teacher: {self.username}"


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


