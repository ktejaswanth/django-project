import pytz
from django import forms
from .models import Blog, Marks, AddCourse


# from .models import Marks
#It will resuce the lines of code in HTML file and views.py.When the no.of parametres in more we can use forms.py This file is not mandatory
# is_valid() - Checks the form whether all the fields are filled or not in the form
# form.save() - saves the information in the database
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','content']

class AddCourseForm(forms.ModelForm):
    class Meta:
        model=AddCourse
        fields=['student','course','section']

class MarksForm(forms.ModelForm):
    class Meta:
        model=Marks
        fields=['student','course','marks']



