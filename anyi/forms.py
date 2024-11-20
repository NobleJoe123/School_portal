from django import forms
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from .models import Role, Student, Teacher
import hashlib

class UserForm(forms.Form):
    fname = forms.CharField(max_length=100)
    sname = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    phonenum = forms.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput)
    image = forms.ImageField()
    role = forms.ModelChoiceField(queryset=Role.objects.all(), empty_label="Select Role")



class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"
        widgets = {
            'password': forms.PasswordInput(),
        }



class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)




class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'fname', 'lname', 'mname', 'username', 'email', 'phonenum',
            'password', 'state', 'country', 'lga', 'dob', 'guardianname',
            'passport', 'address', 'student_class', 'department',
        ]

    # Custom field labels
    labels = {
        'fname': 'First Name',
        'sname': 'Last Name',
        'mname': 'Middle Name',
        'student_class': 'Class',
        'department': 'Department',
        'dob': 'Date of Birth',
        'guardianname': 'Guardian Name',
    }

    # Add widgets for form styling
    widgets = {
        'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        'dob': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
    }



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Update department field dynamically
        self.fields['department'].required = False

        if 'student_class' in self.data:
            student_class = self.data.get('student_class')
            if student_class and student_class.startswith("SS"):  # If SS1, SS2, or SS3
                self.fields['department'].required = True  # Make department required
        elif self.instance and self.instance.student_class:
            if self.instance.student_class.startswith("SS"):  # For editing existing data
                self.fields['department'].required = True

    # Override save method to generate adminum
    def save(self, commit=True):
        instance = super().save(commit=False)

    # Generate adminum or other unique values
        unique_data = f"{instance.fname}{instance.lname}{instance.dob}"
        instance.adminum = hashlib.sha256(unique_data.encode()).hexdigest()[:10]
        
        try:
            if commit:
                instance.save()
        except IntegrityError:
            raise ValidationError("A student with these details already exists.")
        return instance