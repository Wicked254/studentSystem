# students/urls.py

from django.urls import path
from students import views
from django.contrib import admin

urlpatterns = [
    path('student_login/', views.student_login, name='student_login'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('issue_form/', views.issue_form, name='issue_form'),
    path('issue_submitted/', views.issue_submitted, name='issue_submitted'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('', views.landing_page, name='landing_page'),
    path('issue_history/', views.issue_history, name='issue_history'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/', admin.site.urls),
    path('profile/', views.view_profile, name='view_profile'),
    path('view_issues/', views.view_issues, name='view_issues'),
    path('categorize/<int:issue_id>/', views.categorize_issue, name='categorize_issue'),
    path('provide_feedback/<int:issue_id>/', views.provide_feedback, name='provide_feedback'),
    path('filter_issues/', views.filter_issues, name='filter_issues'),
    path('feedback_success/', views.feedback_success, name='feedback_success'),
    path('view_feedback/', views.view_feedback, name='view_feedback'),
    path('admin_feedback/', views.admin_feedback, name='admin_feedback'),
    path('issue-adminlogin/', views.issue_admin_login, name='issue_admin_login'),
    path('issue_list/', views.issue_list, name='issue_list'),
    path('issue_admin_login/', views.issue_admin_login, name='issue_admin_login'),
]
