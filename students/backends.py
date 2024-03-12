from django.contrib.auth.backends import ModelBackend
from .models import Student, Admin

class StudentBackend(ModelBackend):
    def authenticate(self, request, reg_no=None, password=None, **kwargs):
        try:
            student = Student.objects.get(registration_number=reg_no)
        except Student.DoesNotExist:
            return None

        if student.check_password(password):
            return student
        return None

class AdminBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            admin = Admin.objects.get(username=username)
        except Admin.DoesNotExist:
            return None

        if admin.check_password(password):
            return admin
        return None
