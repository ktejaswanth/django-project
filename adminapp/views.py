import base64
import calendar
import random
import string
import datetime
import time
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
import pandas as pd
import pytz
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Contact
from .forms import TaskForm, UploadFileForm, FeedbackForm, ContactForm
from django.contrib import messages
from django.contrib.auth.models import User, auth
from io import BytesIO
#To generate dynamic images we use BytesIO and base64. To send the images to html we need to send it in the form of bytes
#matplotlib genereates the graph
def projecthomepage(request):
    return render(request, "adminapp/ProjectHomePage.html")
def printpagecall(request):
    return render(request,'adminapp/printer.html')
def printpagelogic(request):
    if request.method=="POST":
        user_input=request.POST['user_input']
        print(f'User Input: {user_input}')
    a1={'user_input':user_input}
    return render(request,'adminapp/printer.html',a1)
def randompagecall(request):
    return render(request,'adminapp/randomexample.html')
def randompagelogic(request):
    if request.method=="POST":
        number1=int(request.POST['number1'])
        ran=''.join(random.sample(string.ascii_uppercase+string.digits,k=number1))
    a1={'ran':ran}
    return render(request,'adminapp/randomexample.html',a1)
def exceptionpagecall(request):
    return render(request,'adminapp/exception.html')
def exceptionpagelogic(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        result = None
        error_message = None
        try:
            num = int(user_input)
            result = 10 / num
        except Exception as e:
            error_message = str(e)
        return render(request, 'adminapp/exception.html', {'result': result, 'error': error_message})
    return render(request, 'adminapp/exception')
def calculatorpagecall(request):
    return render(request,'adminapp/calculator.html')
def calculatorpagelogic(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Infinity'
    return render(request, 'adminapp/calculator.html', {'result': result})
def timepagecall(request):
    return render(request,'adminapp/Timepage.html')
def timepagelogic(request):
    if request.method == "POST":
        number1=int(request.POST['date1'])
        x=datetime.now()
        ran=x+timedelta(days=number1)
        ran1=ran.year
        ran2=calendar.isleap(ran1)
        if ran2==False:
            ran3="Not Leap Year"
        else:
            ran3="Leap Year"
    a1={'ran':ran,'ran3':ran3,'ran1':ran1,'number1':number1}
    return render(request, 'adminapp/Timepage.html', a1)
# def addtaskpagecall(request):
#     return render(request,'adminapp/add_task.html')
def registerpagecall(request):
    return render(request,'adminapp/register.html')
def add_task(request):
    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
    else:
        form=TaskForm()
    tasks = Task.objects.all()
    return render(request,'adminapp/add_task.html',{'form':form,'tasks':tasks})
def delete_task(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('add_task')

def loginpagecall(request):
    return render(request,'adminapp/login.html')
def loginpagelogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if len(username) == 10:
                # Redirect to StudentHomePage
                messages.success(request, 'Login successful as student!')
                return redirect('studentapp:StudentHomePage')  # Replace with your student homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            elif len(username) == 4:
                # Redirect to FacultyHomePage
                # messages.success(request, 'Login successful as faculty!')
                return redirect('facultyapp:FacultyHomePage')  # Replace with your faculty homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'adminapp/login.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/login.html')
    else:
        return render(request, 'adminapp/login.html')
def logout(request):
    auth.logout(request)
    return redirect('projecthomepage')
from django.contrib.auth.models import User
from .models import StudentList
from .forms import StudentForm
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            register_number = form.cleaned_data['Register_Number']
            try:
                user = User.objects.get(username=register_number)
                student.user = user  # Assign the matching User to the student
            except User.DoesNotExist:
                form.add_error('Register_Number', 'No user found with this Register Number')
                return render(request, 'adminapp/AddStudent.html', {'form': form})
            student.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'adminapp/AddStudent.html', {'form': form})
def student_list(request):
    students = StudentList.objects.all()
    return render(request, 'adminapp/ViewStudents.html', {'students': students})
#[ ] headings in the csv are kept between the square braces.
def graphpagecall(request):
    return render(request,'adminapp/chart.html')
def graphpagelogic(request):
    if request.method == 'POST' and request.FILES['file']:
        file=request.FILES['file']
        df = pd.read_csv(file, parse_dates=['Date'],dayfirst=True)
        total_sales = df['Sales'].sum()
        average_sales=df['Sales'].mean()
        df['Month']=df['Date'].dt.month
        monthly_sales=df.groupby('Month')['Sales'].sum()
        month_names=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        monthly_sales.index = monthly_sales.index.map(lambda x : month_names[x-1])
        plt.pie(monthly_sales,labels=monthly_sales.index, autopct = '%1.1f%%')
        plt.title('Sales Distribution Per Month')
        buffer = BytesIO()
        plt.savefig(buffer,format='png')
        buffer.seek(0)
        image_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.close()
        return render(request,'adminapp/chart.html' , {
            'total_sales' : total_sales,
            'average_sales': average_sales,
            'chart': image_data,
            'form': UploadFileForm()
        })
    return render(request,'adminapp/chart.html',{'form':UploadFileForm()})
def add_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_feedback')
    else:
        form = FeedbackForm()
    return render(request, 'adminapp/Feedback.html', {'form': form})
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .models import Contact
from .forms import ContactForm
@login_required  # Ensure the user is logged in
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_instance = form.save(commit=False)
            contact_instance.user = request.user  # Associate contact with the logged-in user
            contact_instance.save()
            # Prepare the email content
            subject = 'New Contact Added'
            all_contacts = Contact.objects.filter(user=request.user)
            contacts_list = "\n".join(
                [f'Name: {contact.name}, Email: {contact.email}, Phone: {contact.phone}, Address: {contact.address}' for
                 contact in all_contacts]
            )
            message = f'Hello {request.user.username},\n\nYou have added a new contact:\n\n' \
                      f'Name: {contact_instance.name}\n' \
                      f'Email: {contact_instance.email}\n' \
                      f'Phone: {contact_instance.phone}\n' \
                      f'Address: {contact_instance.address}\n\n' \
                      f'Here are all your contacts:\n{contacts_list}\n\n' \
                      f'Thank you!'
            from_email = ''  # Replace with your email
            recipient_list = [request.user.email]
            send_mail(subject, message, from_email, recipient_list)
            return redirect('add_contact')  # Redirect to the same page or another page
    else:
        form = ContactForm()
    contacts = Contact.objects.filter(user=request.user)  # Only show the logged-in user's contacts
    return render(request, 'adminapp/contact.html', {'form': form, 'contacts': contacts})
from django.shortcuts import get_object_or_404, redirect
from .models import Task
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect('add_contact')
def registerpagelogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['firstname']  # Corrected variable
        last_name = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/register.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,  # Changed here
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'adminapp/ProjectHomepage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/register.html')
    else:
        return render(request, 'adminapp/register.html')
