from django.urls import path,include
from . import views
app_name='studentapp'
# to communicate between the apps we have to mention the app name
urlpatterns = [
    path('', views.StudentHomePage, name='StudentHomePage'),
    path('view_marks/', views.view_marks, name='view_marks'),

]
