
# Create your models here.Tp store any data in database we should write in models.py. This class is stored as a table in the database
#Make migrations: used to convert class to table in the database
from django.db import models
from django.contrib.auth.models import User
class Task(models.Model):
    title= models.CharField(max_length=200)
    created_at= models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

from django.contrib.auth.models import User
class StudentList(models.Model):
    Register_Number = models.CharField(max_length=20, unique=True)
    Name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    def str(self):
        return self.Register_Number

class Feedback(models.Model):
    name= models.CharField(max_length=200)
    email = models.EmailField(max_length=254, blank=False, null=False)
    mobileno=models.CharField(max_length=10)
    feedback=models.CharField(max_length=150)

    def str(self):
        return self.name,self.feedback

class Contact(models.Model):
    name= models.CharField(max_length=200)
    email = models.EmailField(max_length=40, blank=False, null=False)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # Allow null temporarily


    def str(self):
        return self.name,self.phone,self.email,self.address