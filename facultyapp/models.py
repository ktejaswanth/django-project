from django.db import models
from django.db import models
from adminapp .models import StudentList
from django.contrib.auth.models import User
# Create your models here.Tp store any data in database we should write in models.py. This class is stored as a table in the database
#Make migrations: used to convert class to table in the database
class Blog(models.Model):
    title= models.CharField(max_length=200)
    content=models.CharField(max_length=300)

    def str(self):
        return self.title

class AddCourse(models.Model):
    COURSE_CHOICES=[
        ('AOOP','Advanced Object Oriented Programming'),
        ('PFSD', 'Python Full Stack Development'),
        ('DBMS','DataBase Management System'),
        ('LAA', 'Linux Automation and Administration'),
    ]
    SECTION_CHOICES=[
        ('S11','Section11'),
        ('S12', 'Section12'),
        ('S13', 'Section13'),
        ('S14', 'Section14'),
        ('S15', 'Section15'),
    ]
    student=models.ForeignKey(StudentList,on_delete=models.CASCADE)
    course=models.CharField(max_length=50,choices=COURSE_CHOICES)
    section=models.CharField(max_length=50,choices=SECTION_CHOICES)
    def __str__(self):
        return f'{self.student.Register_Number} - {self.course} ({self.section})'

class Marks(models.Model):
    COURSE_CHOICES = [
        ('AOOP', 'Advanced Object Oriented Programming'),
        ('PFSD', 'Python Full Stack Development'),
        ('DBMS', 'DataBase Management System'),
        ('LAA', 'Linux Automation and Administration'),
    ]
    student = models.ForeignKey(StudentList, on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    marks = models.IntegerField()

    def __str__(self):
        return f'{self.student.name} - {self.course} )'