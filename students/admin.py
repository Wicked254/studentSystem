from django.contrib import admin
from .models import Student, Admin, Issue, Complaint

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['username', 'registration_number', 'email', 'first_name', 'last_name']

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name']


