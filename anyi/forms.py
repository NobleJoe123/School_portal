from django import forms
from django.core.exceptions import ValidationError
from .models import Role, jss1, jss2, jss3, ss1, ss2, ss3, Teacher

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




class StudentForm(forms.Form):
    STUDENT_TYPE_CHOICES = [
        ('jss1', 'jss1'),
        ('jss2', 'jss2'),
        ('jss3', 'jss3'),
        ('ss1', 'ss1'),
        ('ss2', 'ss2'),
        ('ss3', 'ss3'),
    ]

    firstname = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    middlename = forms.CharField(max_length=100, required=False)
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    phonenum = forms.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput)
    state = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)
    lga = forms.CharField(max_length=100)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    guardianname = forms.CharField(max_length=100)
    image = forms.ImageField()
    classes = forms.ChoiceField(choices=STUDENT_TYPE_CHOICES)

    def save(self):
        # Get cleaned data from the form
        data = self.cleaned_data
        student_type = data.pop('classes')  # Extract the dropdown value

        # Determine which model to use based on dropdown selection
        if student_type == 'jss1':
            return jss1.objects.create(**data)
        elif student_type == 'jss2':
            return jss2.objects.create(**data)
        elif student_type == 'jss3':
            return jss3.objects.create(**data)
        elif student_type == 'ss1':
            return ss1.objects.create(**data)
        elif student_type == 'ss2':
            return ss2.objects.create(**data)
        elif student_type == 'ss3':
            return ss3.objects.create(**data)
        else:
            raise ValueError("Invalid student type selected")   