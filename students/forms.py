from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Issue, Student,Admin,Feedback

class StudentLoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
class AdminLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    selected_category = forms.ChoiceField(choices=[
        ('healthcare', 'Healthcare'),
        ('fee_issues', 'Fee Issues'),
        ('guidance_and_counselling', 'Guidance and Counselling'),
        ('accommodation', 'Accommodation'),
        ('exam_issues', 'Exam Issues'),
        ('others', 'Others'),
    ])
class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['issue_type', 'description']

class FeedbackForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
class StudentRegistrationForm(UserCreationForm):
    reg_no = forms.CharField(max_length=20, label='Registration Number')
    email = forms.EmailField(max_length=254, label='Email')
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    class Meta:
        model = Student
        fields = ['reg_no', 'email', 'first_name', 'last_name', 'password1', 'password2']

class FeedbackForm(forms.Form):
    feedback_text = forms.CharField(label='Feedback', widget=forms.Textarea)
class IssueAdminForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['issue_type', 'description', 'category', 'issue_admin']

