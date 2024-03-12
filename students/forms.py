from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Issue, Student, Admin,Complaint

class StudentLoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
class AdminLoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['issue_type', 'description']


class StudentRegistrationForm(UserCreationForm):
    reg_no = forms.CharField(max_length=20, label='Registration Number')
    email = forms.EmailField(max_length=254, label='Email')
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    class Meta:
        model = Student
        fields = ['reg_no', 'email', 'first_name', 'last_name', 'password1', 'password2']

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['issue_type', 'description']
class FeedbackForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
