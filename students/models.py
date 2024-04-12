from django.contrib.auth.models import User
from django.db import models
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    registration_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.user.username

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Other fields and methods...

    def __str__(self):
        return f"Admin: {self.user.username}"
class IssueAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ISSUE_CHOICES = [
        ('healthcare', 'Healthcare'),
        ('fee_issues', 'Fee Issues'),
        ('guidance_and_counselling', 'Guidance and Counselling'),
        ('accommodation', 'Accommodation'),
        ('exam_issues', 'Exam Issues'),
        ('others', 'Others'),
    ]
    role = models.CharField(max_length=100, choices=ISSUE_CHOICES)
    def __str__(self):
        return f"IssueAdmin: {self.id}"
class Issue(models.Model):
    ISSUE_CHOICES = [
        ('healthcare', 'Healthcare'),
        ('fee_issues', 'Fee Issues'),
        ('guidance_and_counselling', 'Guidance and Counselling'),
        ('accommodation', 'Accommodation'),
        ('exam_issues', 'Exam Issues'),
        ('others', 'Others'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_issues')
    issue_type = models.CharField(max_length=30, choices=ISSUE_CHOICES)
    description = models.TextField()
    feedback = models.TextField(blank=True)
    category = models.CharField(max_length=100, choices=ISSUE_CHOICES, blank=True, null=True)
    issue_admin = models.ForeignKey(IssueAdmin, on_delete=models.SET_NULL, null=True, blank=True)
    date_submitted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.issue_type} by {self.student.user.username}"

class IssueHistory(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='issue_history')
    issue_type = models.CharField(max_length=100)
    description = models.TextField()
    feedback = models.TextField(blank=True)
    date_submitted = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.issue_type} by {self.student.username}"

class Feedback(models.Model):
    issue = models.ForeignKey('Issue', on_delete=models.CASCADE, related_name='feedbacks') 
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Feedback for Issue {self.issue.id}"