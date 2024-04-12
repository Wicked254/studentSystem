# Generated by Django 5.0.2 on 2024-03-26 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_remove_feedback_user_alter_feedback_issue'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='category',
            field=models.CharField(blank=True, choices=[('healthcare', 'Healthcare'), ('fee_issues', 'Fee Issues'), ('guidance_and_counselling', 'Guidance and Counselling'), ('accommodation', 'Accommodation'), ('exam_issues', 'Exam Issues'), ('others', 'Others')], max_length=100, null=True),
        ),
    ]