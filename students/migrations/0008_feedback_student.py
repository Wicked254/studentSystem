# Generated by Django 5.0.2 on 2024-03-29 14:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_rename_feedback_text_feedback_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='students.student'),
        ),
    ]
