from django.contrib import admin
from .models import Issue, Feedback,IssueAdmin

admin.site.register(Issue)
admin.site.register(IssueAdmin)
admin.site.register(Feedback)