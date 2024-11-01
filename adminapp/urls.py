from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.projecthomepage,name='projecthomepage'),
    path('printpagecall/',views.printpagecall,name='printpagecall'),
    path('printpagelogic/',views.printpagelogic,name='printpagelogic'),
    path('randompagecall/',views.randompagecall,name='randompagecall'),
    path('randompagelogic/',views.randompagelogic,name='randompagelogic'),
    path('exceptionpagecall/',views.exceptionpagecall,name='exceptionpagecall'),
    path('exceptionpagelogic/',views.exceptionpagelogic,name='exceptionpagelogic'),
    path('calculatorpagecall/',views.calculatorpagecall,name='calculatorpagecall'),
    path('calculatorpagelogic/',views.calculatorpagelogic,name='calculatorpagelogic'),
    path('registerpagecall/',views.registerpagecall,name='registerpagecall'),
    path('timepagecall/',views.timepagecall,name='timepagecall'),
    path('timepagelogic/',views.timepagelogic,name='timepagelogic'),
    path('add_task/',views.add_task,name='add_task'),
    path('<int:pk>/delete/',views.delete_task,name='delete_task'),
    path('registerpagecall/',views.registerpagecall,name='registerpagecall'),
    path('registerpagelogic/',views.registerpagelogic,name='registerpagelogic'),
    path('loginpagecall/',views.loginpagecall,name='loginpagecall'),
    path('loginpagelogic/',views.loginpagelogic,name='loginpagelogic'),
    path('logout/',views.logout,name='logout'),
    path('add_student/',views.add_student,name='add_student'),
    path('students/', views.student_list, name='student_list'),
    path('graphpagecall/',views.graphpagecall,name='graphpagecall'),
    path('graphpagelogic/',views.graphpagelogic,name='graphpagelogic'),
    path('add_feedback/',views.add_feedback,name='add_feedback'),
    path('add_contact/',views.add_contact,name='add_contact'),
    path('<int:pk>/delete/', views.delete_contact, name='delete_contact')

]
