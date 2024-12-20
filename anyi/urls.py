
from django.urls import path
from . import views
# search_create





urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('admin_register/', views.admin_register, name='admin_register'),
    path('add_teacher/', views.add_teacher, name='add_teacher'),
    path('add_student/', views.add_student, name='add_student'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('student_login/', views.student_login, name='student_login'),
    path('bursal_login/', views.bursal_login, name='bursal_login'),
    path('teacher_login/', views.teacher_login, name='teacher_login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    # path('teacher_board', views.teacher_board, name='teacher_board'),
    path('bursal_dashboard/', views.bursal_dashboard, name='bursal_dashboard'),
    path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('enrol/', views.enrol, name='enrol'),
    path('admin_enrol/', views.admin_enrol, name='admin_enrol'),
    path('student_reg/', views.student_register, name='student_reg'),
    # path('404/', views.custom_404_view, name='404'),
    

   
] 

# handler404 = "anyi.views.custom_404_view"