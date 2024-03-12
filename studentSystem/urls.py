# students/urls.py

from django.urls import path
from students import views
from django.contrib import admin

urlpatterns = [
    path('student_login/', views.student_login, name='student_login'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('issue_form/', views.issue_form, name='issue_form'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('issue_submitted/', views.issue_submitted, name='issue_submitted'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('', views.landing_page, name='landing_page'),
    path('complaint_history/', views.complaint_history, name='complaint_history'),  # New URL for complaint_history
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('admin/', admin.site.urls),
]
