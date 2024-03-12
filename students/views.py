# views.py

from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import (
    StudentLoginForm, AdminLoginForm, IssueForm, 
    StudentRegistrationForm,FeedbackForm
)
from .models import Student, Admin, Issue, Complaint,Feedback
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def student_login(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('student_login')
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password) 
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('student_login')
        else:
            # Log in the user and redirect to the issueform page upon successful login
            login(request, user)
            return redirect('issue_form')
    # Render the issue form template (GET request)
    return render(request, 'student_login.html')
def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'], 
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('admin_dashboard')
    else:
        form = AdminLoginForm()
    return render(request, 'admin_login.html', {'form': form})

def issue_form(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.student = request.user
            issue.save()
            return redirect('issue_submitted')
    else:
        form = IssueForm()
    return render(request, 'issue_form.html', {'form': form})

def admin_dashboard(request):
    issues = Issue.objects.all()
    feedback = Feedback.objects.all()

    context = {
        'issues': issues,
        'feedback': feedback,
    }

    return render(request, 'admin_dashboard.html', context)

@login_required(login_url='login')
def provide_feedback(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback_text = form.cleaned_data['text']

            # Create Feedback object and save it
            feedback = Feedback(issue=issue, text=feedback_text)
            feedback.save()

            messages.success(request, 'Feedback provided successfully.')
            return redirect('admin_dashboard')
    else:
        form = FeedbackForm()

    context = {
        'issue': issue,
        'form': form,
    }

    return render(request, 'provide_feedback.html', context)

def issue_submitted(request):
    return render(request, 'issue_submitted.html')

def logout_view(request):
    logout(request)
    return redirect('home')


def register(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        E
        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)
        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('/register/')
        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        # Set the user's password and save the user object
        user.set_password(password)
        user.save()
        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect('student_login')
     
    # Render the registration page template (GET request)
    return render(request, 'register.html')
    

def landing_page(request):
    return render(request, 'landing_page.html')

def student_dashboard(request):
    if request.user.is_authenticated and isinstance(request.user, Student):
        # Redirect to the issue form if the user is authenticated and is a student
        return redirect('issue_form')
    else:
        return redirect('student_login')  # Redirect to student login if not authenticated or not a student
    
    
def complaint_history(request):
    # Fetch student's complaint history
    student_complaints = Issue.objects.filter(student=request.user)

    context = {
        'complaints': student_complaints,
    }

    return render(request, 'complaint_history.html', context)