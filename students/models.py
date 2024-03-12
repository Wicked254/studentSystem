from django.db import models
from django.contrib.auth.models import User


class Student(User):
    # Inherits from User model, so fields like username, password, email, etc. are already included
    registration_number = models.CharField(max_length=20, unique=True)

class Admin(User):
    # Inherits from User model, so fields like username, password, email, etc. are already included
    pass

class Issue(models.Model):
    ISSUE_CHOICES = [
        ('healthcare', 'Healthcare'),
        ('fee_issues', 'Fee Issues'),
        ('guidance_and_counselling', 'Guidance and Counselling'),
        ('accommodation', 'Accommodation'),
        ('exam_issues', 'Exam Issues'),
        ('others', 'Others'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='issues')
    issue_type = models.CharField(max_length=30, choices=ISSUE_CHOICES)
    description = models.TextField()
    feedback = models.TextField(blank=True)
    admin = models.ForeignKey(Admin, on_delete=models.SET_NULL, null=True, related_name='resolved_issues')

    def __str__(self):
        return f"{self.issue_type} by {self.student.username}"
    # models.py

class Complaint(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    issue_type = models.CharField(max_length=100)
    description = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='feedback_items')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username if self.user else "Anonymous"} - {self.created_at}'
    def __str__(self):
        return f"{self.student} - {self.issue_type} - {self.date_submitted}"

