app_name='facultyapp'
from django.urls import path
from . import views

urlpatterns = [
    path('', views.FacultyHomePage, name='FacultyHomePage'),
path('addblogpagecall/',views.addblogpagecall,name='addblogpagecall'),
path('add_blog/',views.add_blog,name='add_blog'),
path('<int:pk>/delete/',views.delete_blog,name='delete_blog'),
path('add_course/',views.add_course,name='add_course'),
path('post_marks/',views.post_marks,name='post_marks'),
path('view_student_list/',views.view_student_list,name='view_student_list'),

]

