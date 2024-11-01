import pytz
from django import forms
from .models import Task, Feedback, StudentList, Contact
#It will resuce the lines of code in HTML file and views.py.When the no.of parametres in more we can use forms.py This file is not mandatory
# is_valid() - Checks the form whether all the fields are filled or not in the form
# form.save() - saves the information in the database
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','phone','address']
class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentList
        fields = ['Register_Number', 'Name']

class UploadFileForm(forms.Form):
    file = forms.FileField()

# class FeedbackForm(forms.ModelForm):
#     class Meta:
#         model = Feedback
#         fields = ['name','email','mobileno','feedback']
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'mobileno', 'feedback']
        widgets = {
            'feedback': forms.Textarea(attrs={
                'rows': 4,
                'cols': 40,
                'placeholder': 'Enter your feedback here...',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['feedback'].max_length = 150
        self.fields['feedback'].error_messages = {
            'max_length': 'Feedback cannot exceed 150 characters.'
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise ValidationError('This email does not exist in our records.')
        return email
