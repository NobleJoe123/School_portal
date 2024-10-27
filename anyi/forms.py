from django import forms
from django.core.exceptions import ValidationError
from .models import Role, Admin, Bursal, Teacher

class UserForm(forms.Form):
    fname = forms.CharField(max_length=100)
    sname = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    phonenum = forms.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ModelChoiceField(queryset=Role.objects.all(), empty_label="Select Role")


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)