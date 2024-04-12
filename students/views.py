# views.py

from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import (
    StudentLoginForm, AdminLoginForm, IssueForm, 
    StudentRegistrationForm,FeedbackForm
)
from .models import Student, Admin , Issue, Feedback
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.sessions.models import Session


def student_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the student with the provided username and password
        student = authenticate(request, username=username, password=password) 
        if student is not None:
            login(request, student)  # Log in the student
            return redirect('student_dashboard')  # Redirect to student dashboard
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'student_login.html')
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        category = request.POST.get('category')  # Get selected category
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:  # Assuming admins are superusers
                login(request, user)
                # Store the selected category in session
                request.session['selected_category'] = category
                return redirect('admin_dashboard')  # Redirect to admin dashboard
            else:
                # User is not an admin, display error message
                error_message = "You are not authorized to access the admin dashboard."
        else:
            # Authentication failed, display error message
            error_message = "Invalid username or password."
    else:
        error_message = None

    return render(request, 'admin_login.html', {'error_message': error_message})
@login_required(login_url='admin_login')
def admin_dashboard(request):
    # Implement logic to retrieve data for admin dashboard
    return render(request, 'admin_dashboard.html')
def issue_form(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            # Get the current logged-in user
            user = request.user
            # Get the associated student instance
            student = Student.objects.get(user=user)
            
            # Create a new Issue object with the associated student
            issue = form.save(commit=False)
            issue.student = student  # Assign the student instance
            issue.save()
            return redirect('issue_submitted')
    else:
        form = IssueForm()
    return render(request, 'issue_form.html', {'form': form})
def issue_admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to issue admin dashboard or another page
                return redirect('issue_list')
            else:
                # Handle inactive user
                pass
        else:
            # Handle invalid login
            error_message = "Invalid username or password"
            return render(request, 'issuelogin.html', {'error_message': error_message})
    else:
        return render(request, 'issue_adminlogin.html')
def issue_list(request):
    if request.method == 'POST':
        # Retrieve selected category from the form data
        category = request.POST.get('category')
        
        # Filter issues based on the selected category
        issues = Issue.objects.filter(category=category)
        
        # Pass filtered issues to the template
        return render(request, 'issue_list.html', {'issues': issues})
    else:
        # Render the login page template
        return render(request, 'issue_adminlogin.html')

@login_required(login_url='admin_login')
def provide_feedback(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback_text = form.cleaned_data['feedback_text']
            admin = request.user if request.user.is_authenticated else None
            feedback = Feedback.objects.create(issue=issue, text=feedback_text, admin=admin)
            # Delete the issue after providing feedback
            issue.delete()
            # Add a success message
            messages.success(request, 'Feedback submitted successfully.')
            return redirect('feedback_submitted')
    else:
        form = FeedbackForm()

    return render(request, 'provide_feedback.html', {'form': form, 'issue': issue})
def feedback_success(request):
    return render(request, 'feedback_success.html')
def issue_submitted(request):
    return render(request, 'issue_submitted.html')
@login_required(login_url='admin_login')  # Adjust the login URL as needed
def provide_feedback(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback_text = form.cleaned_data['feedback_text']
            Feedback.objects.create(issue=issue, text=feedback_text, admin=request.user)
            return redirect('feedback_success')  # Redirect to view issues page after feedback submission
    else:
        form = FeedbackForm()

    return render(request, 'provide_feedback.html', {'form': form, 'issue': issue})
def feedback_success(request):
    return render(request, 'feedback_success.html')
def logout_view(request):
    logout(request)
    return redirect('student_login') 

def register(request):
    if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        registration_number = request.POST.get('registration_number')  # Add registration number field

        # Check if a user with the provided username or email already exists
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            messages.info(request, "Username or Email already taken!")
            return redirect('/register/')

        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email
        )
        user.set_password(password)
        user.save()

        # Create a corresponding Student object
        student = Student.objects.create(
            user=user,
            registration_number=registration_number,
            # Add other fields specific to the Student model
        )

        messages.info(request, "Account created successfully!")
        return redirect('student_login')

    return render(request, 'register.html')

def landing_page(request):
    return render(request, 'landing_page.html')

@login_required(login_url='student_login')
def student_dashboard(request):
    student = request.user  # Assuming Student is a model in your application
    issue = Issue.objects.first()
    context = {
        'student': student,
        'issue': issue
    }

    return render(request, 'student_dashboard.html', context)
    
@login_required(login_url='student_login')
def issue_history(request):
    # Retrieve all submitted issues from the database
    issues = Issue.objects.all()
    return render(request, 'issue_history.html', {'issues': issues})
@login_required(login_url='student_login')
def view_profile(request):
    student = request.user  # Assuming Student is a model in your application

    context = {
        'student': student,
    }

    return render(request, 'profile.html', context)

@login_required(login_url='student_login')
def view_profile(request):
    student = request.user  # Assuming Student is a model in your application

    context = {
        'student': student,
    }

    return render(request, 'profile.html', context)
@login_required(login_url='student_login')
def issue_history(request):
    # Get the currently logged-in student
    student = request.user.student_profile  # Assuming you have a UserProfile linked to the User model

    # Query all issues submitted by the current student
    issue_history = Issue.objects.filter(student=student)

    # Pass the issue history to the template for rendering
    return render(request, 'issue_history.html', {'issue_history': issue_history})
@login_required(login_url='student_login')
def view_feedback(request):
    # Assuming 'student_profile' is the related_name for the Student model in the User model
    student = request.user.student_profile

    # Retrieve all issues related to the student
    issues = Issue.objects.filter(student=student)

    # Create a dictionary to store issues along with their feedbacks
    issues_with_feedback = {}
    for issue in issues:
        # Retrieve feedbacks for the current issue
        feedbacks = Feedback.objects.filter(issue=issue)
        issues_with_feedback[issue] = feedbacks

    return render(request, 'view_feedback.html', {'issues_with_feedback': issues_with_feedback})
@login_required(login_url='admin_login')
def admin_feedback(request):
    # Retrieve all feedbacks associated with the admin user
    feedbacks = Feedback.objects.filter(admin=request.user)

    return render(request, 'admin_feedback.html', {'feedbacks': feedbacks})
@login_required(login_url='admin_login')

def view_issues(request):
    # Retrieve the selected category from the session
    selected_category = request.session.get('selected_category')

    # Filter issues based on the selected category
    if selected_category:
        issues = Issue.objects.filter(issue_type=selected_category)
    else:
        # If no category is selected, retrieve all issues
        issues = Issue.objects.all()

    # Pass issue choices to the template context
    ISSUE_CHOICES = [
        ('healthcare', 'Healthcare'),
        ('fee_issues', 'Fee Issues'),
        ('guidance_and_counselling', 'Guidance and Counselling'),
        ('accommodation', 'Accommodation'),
        ('exam_issues', 'Exam Issues'),
        ('others', 'Others'),
    ]

    context = {
        'issues': issues,
        'selected_category': selected_category,  # Pass selected category to template
        'ISSUE_CHOICES': ISSUE_CHOICES,
    }

    return render(request, 'issues.html', context)
def filter_issues(request):
    category = request.GET.get('category')
    filtered_issues = Issue.objects.filter(issue_type=category)
    return render(request, 'filtered_issues.html', {'filtered_issues': filtered_issues})
def categorize_issue(request, issue_id):
    # Fetch the issue based on the provided ID
    issue = Issue.objects.get(id=issue_id)

    if request.method == 'POST':
        # Get the selected category from the form data
        category = request.POST.get('category')

        # Update the issue with the selected category
        issue.category = category
        issue.save()

        # Redirect back to the view issues page
        return redirect('view_issues')

    return render(request, 'categorize_issue.html', {'issue': issue})