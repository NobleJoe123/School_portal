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
