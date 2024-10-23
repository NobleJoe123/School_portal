
from django.urls import path
from .views import home, about, courses, admin_register, admin_login, student_login, bursal_login, teacher_login, enrol, user_enrol
# search_create






urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('courses/', courses, name='courses'),
    path('admin_register/', admin_register, name='admin_register'),
    path('admin_login/', admin_login, name='admin_login'),
    path('student_login/', student_login, name='student_login'),
    path('bursal_login/', bursal_login, name='bursal_login'),
    path('teacher_login/', teacher_login, name='teacher_login'),
    path('enrol/', enrol, name='enrol'),
    path('user_enrol/', user_enrol, name='user_enrol'),

   
]